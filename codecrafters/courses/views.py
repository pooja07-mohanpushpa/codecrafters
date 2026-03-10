from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, UserProgress, UserAchievement
from users.models import UserProfile


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
def arena_view(request):
    """Placeholder for Algorithm Arena."""
    return render(request, 'courses/arena.html')


@login_required
def quiz_view(request):
    """Placeholder for AI Quiz."""
    return render(request, 'courses/quiz.html')
