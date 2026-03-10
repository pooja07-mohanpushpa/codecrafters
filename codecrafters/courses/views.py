from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import Course, Topic, UserProgress, UserAchievement, QuizAttempt
from users.models import UserProfile
import json
import random


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

        course_data.append({
            'course':     course,
            'total':      total,
            'done':       done,
            'pct':        pct,
            'stars':      stars,
            'stars_range':  range(stars),
            'empty_range':  range(5 - stars),
        })

    # ── Global Leaderboard (top 3 by CodePoints for Home page) ────────────
    leaderboard = (
        UserProfile.objects
        .select_related('user')
        .order_by('-code_points')[:3]
    )

    # ── Current Course Selection ──────────────────────────────────────────
    current_course = None
    for cd in course_data:
        if 0 < cd['pct'] < 100:
            current_course = cd
            break
    if not current_course and course_data:
        current_course = course_data[0]

    # ── User Achievements ─────────────────────────────────────────────────
    user_achievements = UserAchievement.objects.filter(user=user).select_related('achievement')

    context = {
        'profile':          profile,
        'current_course':   current_course,
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
    for topic in course.topics.all():
        topics_with_status.append({
            'topic': topic,
            'is_completed': topic.id in completed_topic_ids,
        })

    context = {
        'course': course,
        'topics': topics_with_status,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def topic_detail_view(request, topic_id):
    """
    Shows the lesson content/video for a specific topic.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    # Check progress
    progress, created = UserProgress.objects.get_or_create(user=request.user, topic=topic)
    
    # Get previous and next topics for navigation
    prev_topic = Topic.objects.filter(course=topic.course, order__lt=topic.order).order_by('-order').first()
    next_topic = Topic.objects.filter(course=topic.course, order__gt=topic.order).order_by('order').first()

    context = {
        'topic': topic,
        'profile': profile,
        'progress': progress,
        'prev_topic': prev_topic,
        'next_topic': next_topic,
    }
    return render(request, 'courses/topic_detail.html', context)


@login_required
def generate_quiz(request, topic_id):
    """
    AJAX view to generate 5 MCQs using AI (Gemini).
    """
    topic = get_object_or_404(Topic, id=topic_id)
    
    # In a real app, you'd call Gemini API here.
    # Instruction: "Generate 5 MCQ questions with four options and mark the correct answer."
    
    # Mocking AI response for the demo
    mock_questions = [
        {
            "id": 1,
            "question": f"What is a core concept in {topic.title}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct": 0
        },
        {
            "id": 2,
            "question": f"Which of these best describes {topic.title}?",
            "options": ["Variable", "Function", "Logic", "Data"],
            "correct": 1
        },
        {
            "id": 3,
            "question": f"When implementing {topic.title}, what is most important?",
            "options": ["Speed", "Memory", "Readability", "Syntax"],
            "correct": 2
        },
        {
            "id": 4,
            "question": f"A common error when using {topic.title} is...",
            "options": ["Syntax Error", "Logic Error", "Null Pointer", "Stack Overflow"],
            "correct": 1
        },
        {
            "id": 5,
            "question": f"Why do we use {topic.title}?",
            "options": ["Efficiency", "Organization", "Automation", "Security"],
            "correct": 0
        }
    ]
    
    # Shuffle options slightly for realism
    for q in mock_questions:
        correct_answer = q['options'][q['correct']]
        random.shuffle(q['options'])
        q['correct'] = q['options'].index(correct_answer)

    return JsonResponse({"questions": mock_questions})


@login_required
def submit_quiz(request, topic_id):
    """
    AJAX view to score the quiz and award points.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score', 0) # 0 to 5
        
        topic = get_object_or_404(Topic, id=topic_id)
        points_earned = score * 10 # 10 pts per correct answer
        
        # Check if user already earned points for this topic to prevent farming
        already_fully_earned = QuizAttempt.objects.filter(user=request.user, topic=topic, score=5).exists()
        if already_fully_earned:
            points_earned = 0
        else:
            # If not 5 yet, we only award the difference if they improve, 
            # or for simplicity here, we only award points on the first success/attempt.
            # Let's go with: Only award on first success per topic or first few attempts.
            # Re-evaluating: Requirement says "Prevent repeated attempts from generating unlimited points".
            if UserProgress.objects.filter(user=request.user, topic=topic, is_completed=True).exists():
                points_earned = 0

        # Save attempt
        QuizAttempt.objects.create(
            user=request.user,
            topic=topic,
            score=score,
            codepoints_earned=points_earned
        )
        
        # Update progress
        progress, _ = UserProgress.objects.get_or_create(user=request.user, topic=topic)
        if score >= 3: # Pass threshold
            progress.is_completed = True
            progress.completed_at = timezone.now()
            progress.save()
        
        # Update user profile points
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

