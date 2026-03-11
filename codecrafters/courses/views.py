from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from .models import Course, Topic, UserProgress, UserAchievement, QuizAttempt
from users.models import UserProfile
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
try:
    import google.generativeai as genai
except ImportError:
    genai = None


@login_required
def dashboard_view(request):
    """
    Main dashboard — pulls real data from the database for the logged-in user.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    # ── Course data with per-user completion % ─────────────────────────────
    all_courses = Course.objects.prefetch_related('topics').order_by('order')

    course_data = []
    for course in all_courses:
        total   = course.topics.count()
        done    = UserProgress.objects.filter(user=user, topic__course=course, is_completed=True).count()
        pct     = int((done / total) * 100) if total > 0 else 0
        stars   = pct // 20   # 1 star per 20%

        # A course is "started" if the user has ANY UserProgress object linked to its topics
        has_started = UserProgress.objects.filter(user=user, topic__course=course).exists()

        course_data.append({
            'course':     course,
            'total':      total,
            'done':       done,
            'pct':        pct,
            'stars':      stars,
            'has_started': has_started,
            'stars_range':  range(stars),
            'empty_range':  range(5 - stars),
        })

    # ── Global Leaderboard (top 3 by PathPoints for Home page) ────────────
    leaderboard = (
        UserProfile.objects
        .select_related('user')
        .order_by('-code_points')[:3]
    )

    # ── Enrolled Courses Selection ──────────────────────────────────────────
    enrolled_courses = []
    for cd in course_data:
        if cd['has_started']:
            enrolled_courses.append(cd)
            
    # If no courses are started, default to suggesting the very first course
    if not enrolled_courses and course_data:
        enrolled_courses = [course_data[0]]

    # ── User Achievements ─────────────────────────────────────────────────
    user_achievements = UserAchievement.objects.filter(user=user).select_related('achievement')

    context = {
        'profile':          profile,
        'enrolled_courses': enrolled_courses,
        'leaderboard':      leaderboard,
        'user_achievements': user_achievements,
    }
    return render(request, 'courses/dashboard.html', context)


@login_required
def courses_view(request):
    """
    Shows all available courses.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    all_courses = Course.objects.prefetch_related('topics').order_by('order')
    course_data = []
    for course in all_courses:
        total   = course.topics.count()
        done    = UserProgress.objects.filter(user=user, topic__course=course, is_completed=True).count()
        pct     = int((done / total) * 100) if total > 0 else 0
        stars   = pct // 20

        course_data.append({
            'course':     course,
            'total':      total,
            'done':       done,
            'pct':        pct,
            'stars':      stars,
            'stars_range':  range(stars),
            'empty_range':  range(5 - stars),
        })

    context = {
        'profile': profile,
        'course_data': course_data,
    }
    return render(request, 'courses/courses.html', context)


@login_required
def leaderboard_view(request):
    """
    Shows the full leaderboard.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    leaderboard = (
        UserProfile.objects
        .select_related('user')
        .order_by('-code_points')
    )

    context = {
        'profile': profile,
        'leaderboard': leaderboard,
    }
    return render(request, 'courses/leaderboard.html', context)


@login_required
def course_detail_view(request, course_id):
    """
    Shows the list of topics for a specific course.
    """
    course = Course.objects.prefetch_related('topics').get(id=course_id)
    # Get user progress for these topics
    user_progress = UserProgress.objects.filter(user=request.user, topic__course=course)
    completed_topic_ids = user_progress.filter(is_completed=True).values_list('topic_id', flat=True)

    topics_with_status = []
    is_previous_completed = True
    for topic in course.topics.all().order_by('order'):
        topic_completed = topic.id in completed_topic_ids
        topics_with_status.append({
            'topic': topic,
            'is_completed': topic_completed,
            'is_locked': not is_previous_completed,
        })
        is_previous_completed = topic_completed

    # Look for a completed Certificate
    from .models import Certificate
    certificate = Certificate.objects.filter(user=request.user, course=course).first()

    context = {
        'course': course,
        'topics': topics_with_status,
        'certificate': certificate,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def topic_detail_view(request, topic_id):
    """
    Shows the lesson content/video for a specific topic.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    # Get previous and next topics for navigation
    prev_topic = Topic.objects.filter(course=topic.course, order__lt=topic.order).order_by('-order').first()
    next_topic = Topic.objects.filter(course=topic.course, order__gt=topic.order).order_by('order').first()

    # Enforce sequential progression
    if prev_topic:
        prev_progress = UserProgress.objects.filter(user=request.user, topic=prev_topic, is_completed=True).exists()
        if not prev_progress:
            from django.contrib import messages
            messages.warning(request, "You must complete the previous topic's quiz before proceeding.")
            return redirect('course_detail', course_id=topic.course.id)
            
    # Check progress (after validating sequential access)
    progress, created = UserProgress.objects.get_or_create(user=request.user, topic=topic)

    context = {
        'topic': topic,
        'profile': profile,
        'progress': progress,
        'prev_topic': prev_topic,
        'next_topic': next_topic,
    }
    return render(request, 'courses/topic_detail.html', context)


@login_required
@login_required
def generate_quiz(request, topic_id):
    """
    Returns stored quiz questions for the topic.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    
    # Strictly use the AI-generated (or seeded) predefined quiz from the DB!
    if topic.predefined_quiz:
        mock_questions = topic.predefined_quiz
    else:
        # Fallback for other courses or if seeding failed
        course_title = topic.course.title.lower() if topic.course else ""
        if "c " in course_title or course_title == "c" or "c programming" in course_title:
            mock_questions = [
                {
                    "id": 1,
                    "question": f"In C, how does {topic.title} interact with memory?",
                    "options": ["Automatic GC", "Manual allocation & pointers", "Virtual DOM", "Reference counting"],
                    "correct": 1
                },
                {
                    "id": 2,
                    "question": "Which of these is used for console output in C?",
                    "options": ["print()", "console.log()", "printf()", "cout"],
                    "correct": 2
                },
                {
                    "id": 3,
                    "question": "C code is transformed into machine code using a:",
                    "options": ["Interpreter", "Compiler", "Virtual Machine", "Transpiler"],
                    "correct": 1
                },
                {
                    "id": 4,
                    "question": f"To use standard I/O features in C alongside {topic.title}, you must:",
                    "options": ["import stdio", "#include <stdio.h>", "require('stdio')", "using namespace std"],
                    "correct": 1
                },
                {
                    "id": 5,
                    "question": "In C, strings are represented as:",
                    "options": ["String objects", "Immutable arrays", "Null-terminated char arrays", "Lists"],
                    "correct": 2
                }
            ]
        else:
            return JsonResponse({
                "error": "Quiz not yet available for this topic. Please try again later.",
                "questions": []
            })
    
    # Shuffle options slightly for realism
    import random
    for q in mock_questions:
        correct_answer = q['options'][q['correct']]
        random.shuffle(q['options'])
        q['correct'] = q['options'].index(correct_answer)

    return JsonResponse({"questions": mock_questions})


@login_required
def submit_quiz(request, topic_id):
    """
    AJAX view to score the quiz and award points securely.
    """
    from django.utils import timezone
    from .models import CourseProgress
    
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score', 0) # 0 to 5
        
        topic = get_object_or_404(Topic, id=topic_id)
        
        progress, created = UserProgress.objects.get_or_create(user=request.user, topic=topic)
        
        # 1. Anti-Farming: Calculate Delta Points
        new_quiz_points = score * 10
        old_quiz_points = progress.highest_quiz_score * 10
        points_earned = max(0, new_quiz_points - old_quiz_points)
        
        if score > progress.highest_quiz_score:
            progress.highest_quiz_score = score
            progress.save()

        QuizAttempt.objects.create(
            user=request.user,
            topic=topic,
            score=score,
            pathpoints_earned=points_earned
        )
        
        # 2. Topic Completion & Course Progress Tracking
        if score >= 3 and not progress.is_completed:
            progress.is_completed = True
            progress.completed_at = timezone.now()
            progress.save()
            points_earned += topic.points_reward  # Add completion bonus once
            
            # Update Course % and Stars
            cp, _ = CourseProgress.objects.get_or_create(user=request.user, course=topic.course)
            cp.topics_completed += 1
            total_topics = topic.course.topics.count()
            if total_topics > 0:
                cp.progress_percentage = round((cp.topics_completed / total_topics) * 100, 1)
                cp.stars_earned = int(cp.progress_percentage // 20)
            cp.save()
            
            # Generate Certificate if 100% completed
            if cp.progress_percentage >= 100:
                from .models import Certificate
                Certificate.objects.get_or_create(user=request.user, course=topic.course)

        # Update total user points
        profile = request.user.profile
        profile.code_points += points_earned
        profile.save()
        
        return JsonResponse({
            "status": "success",
            "score": score,
            "points_earned": points_earned,
            "total_points": profile.code_points
        })

    return JsonResponse({"status": "error"}, status=400)


@login_required
def download_certificate(request, certificate_id):
    """
    Returns the PDF bytes for a given Certificate ID securely.
    """
    from .models import Certificate
    from .utils import generate_certificate_pdf
    from django.http import HttpResponse
    
    cert = get_object_or_404(Certificate, certificate_id=certificate_id)
    
    # Ensure users can only download their own certificates
    if cert.user != request.user:
        return HttpResponse("Unauthorized", status=403)
        
    pdf_bytes = generate_certificate_pdf(cert)
    
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cert.course.title}_Certificate.pdf"'
    return response

@login_required
def rewards_view(request):
    """
    Displays the user's earned certificates and a showcase of community achievements.
    Now also includes Course Badges based on progress stars.
    """
    from .models import Certificate, Course, UserProgress
    from django.contrib.auth.models import User
    
    user_certificates = Certificate.objects.filter(user=request.user)
    
    # Fetch demo certificates for Jenny and Mike to show in "Community Achievements"
    demo_users = User.objects.filter(username__in=['jenny', 'mike'])
    community_certificates = Certificate.objects.filter(user__in=demo_users).exclude(user=request.user)
    
    # Calculate Course Badges for the current user
    all_courses = Course.objects.prefetch_related('topics').order_by('order')
    course_badges = []
    for course in all_courses:
        total = course.topics.count()
        done = UserProgress.objects.filter(user=request.user, topic__course=course, is_completed=True).count()
        pct = int((done / total) * 100) if total > 0 else 0
        stars = pct // 20
        if stars > 0:
            course_badges.append({
                'course': course,
                'stars': stars,
                'pct': pct,
            })
    
    context = {
        'user_certificates': user_certificates,
        'community_certificates': community_certificates,
        'course_badges': course_badges,
        'profile': request.user.profile
    }
    return render(request, 'courses/rewards.html', context)
