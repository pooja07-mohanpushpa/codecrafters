from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from courses.models import Course, UserProgress


def login_view(request):
    """
    Handles GET (show form) and POST (authenticate user).
    On success redirects to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}! 🚀")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'users/login.html')


def register_view(request):
    """
    Handles GET (show form) and POST (create user).
    On success logs user in and redirects to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        # --- Validation ---
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif password != password_confirm:
            messages.error(request, "Passwords do not match. Please try again.")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken. Please choose another.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "An account with that email already exists. Try logging in.")
        else:
            # Create user and log in
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, f"Account created! Welcome to CodeCrafters, {username}! 🎉")
            return redirect('dashboard')

    return render(request, 'users/register.html')


def logout_view(request):
    """
    Logs the user out and redirects to login page.
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out. See you soon!")
    return redirect('login')


@login_required
def profile_view(request):
    """
    User profile panel — shows stats, streak, XP level, heatmap,
    rank card, recent activity, badges, editable bio, and account settings.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    # ── Handle Bio/Status Update (POST) ──
    if request.method == 'POST' and 'update_bio' in request.POST:
        bio_text = request.POST.get('bio', '').strip()[:120]
        status = request.POST.get('status_emoji', '🚀')
        linkedin = request.POST.get('linkedin_url', '').strip()
        profile.bio = bio_text
        profile.status_emoji = status
        profile.linkedin_url = linkedin
        profile.save()
        messages.success(request, "Profile updated! ✨")
        return redirect('profile')

    all_courses = Course.objects.prefetch_related('topics').order_by('order')
    course_data = []
    total_topics_done = 0
    courses_started = 0
    courses_completed = 0

    # Fetch Certificates
    from courses.models import Certificate
    certificates = Certificate.objects.filter(user=user).select_related('course')
    cert_map = {cert.course.id: cert for cert in certificates}

    for course in all_courses:
        total = course.topics.count()
        done  = UserProgress.objects.filter(user=user, topic__course=course, is_completed=True).count()
        pct   = int((done / total) * 100) if total > 0 else 0
        stars = pct // 20
        total_topics_done += done
        if done > 0:
            courses_started += 1
        if pct == 100:
            courses_completed += 1

        course_data.append({
            'course':      course,
            'total':       total,
            'done':        done,
            'pct':         pct,
            'stars':       stars,
            'stars_range': range(stars),
            'empty_range': range(5 - stars),
            'certificate': cert_map.get(course.id),
        })

    # Achievements
    from courses.models import UserAchievement, QuizAttempt
    from arena.models import UserSubmission
    from django.utils import timezone
    from datetime import timedelta
    import itertools, json, collections

    user_achievements = UserAchievement.objects.filter(user=user).select_related('achievement')

    # ── XP Level System ──
    xp_total = profile.code_points
    xp_per_level = 500
    xp_level = xp_total // xp_per_level
    xp_in_level = xp_total % xp_per_level
    xp_pct = int((xp_in_level / xp_per_level) * 100) if xp_per_level > 0 else 0

    # ── Gather All Activity Dates ──
    today = timezone.now().date()
    quiz_dates = list(
        QuizAttempt.objects.filter(user=user)
        .values_list('attempted_at', flat=True)
    )
    submission_dates = list(
        UserSubmission.objects.filter(user=user)
        .values_list('submitted_at', flat=True)
    )
    progress_dates = list(
        UserProgress.objects.filter(user=user, is_completed=True, completed_at__isnull=False)
        .values_list('completed_at', flat=True)
    )

    all_activity_dates = []
    for dt in itertools.chain(quiz_dates, submission_dates, progress_dates):
        if dt:
            all_activity_dates.append(dt.date() if hasattr(dt, 'date') else dt)

    all_dates_set = set(all_activity_dates)

    # ── Streak Calculation ──
    streak = 0
    check_day = today
    while check_day in all_dates_set:
        streak += 1
        check_day -= timedelta(days=1)
    if streak == 0 and (today - timedelta(days=1)) in all_dates_set:
        check_day = today - timedelta(days=1)
        while check_day in all_dates_set:
            streak += 1
            check_day -= timedelta(days=1)

    # ── Activity Heatmap (last 365 days) ──
    date_counts = collections.Counter(all_activity_dates)
    heatmap_data = []
    for i in range(364, -1, -1):
        d = today - timedelta(days=i)
        heatmap_data.append({
            'date': d.isoformat(),
            'count': date_counts.get(d, 0),
            'dow': d.weekday(),  # 0=Mon, 6=Sun
        })
    heatmap_json = json.dumps(heatmap_data)
    total_active_days = len(set(d for d in all_activity_dates if d >= today - timedelta(days=365)))

    # ── Rank Comparison Card ──
    top_user = UserProfile.objects.order_by('-code_points').first()
    top_points = top_user.code_points if top_user else 0

    # ── Recent Activity Timeline ──
    activities = []
    for qa in QuizAttempt.objects.filter(user=user).select_related('topic', 'topic__course').order_by('-attempted_at')[:10]:
        activities.append({
            'type': 'quiz',
            'icon': 'fa-solid fa-brain',
            'color': 'text-purple-500',
            'bg': 'bg-purple-50',
            'text': f'Scored {qa.score}/5 on {qa.topic.title} Quiz',
            'sub': qa.topic.course.title,
            'time': qa.attempted_at,
        })
    for sub in UserSubmission.objects.filter(user=user).select_related('problem').order_by('-submitted_at')[:10]:
        is_pass = sub.status == 'Passed'
        activities.append({
            'type': 'arena',
            'icon': 'fa-solid fa-code' if is_pass else 'fa-solid fa-xmark',
            'color': 'text-emerald-500' if is_pass else 'text-red-400',
            'bg': 'bg-emerald-50' if is_pass else 'bg-red-50',
            'text': f'{"Solved" if is_pass else "Attempted"} "{sub.problem.title}" in Arena',
            'sub': sub.language.capitalize(),
            'time': sub.submitted_at,
        })
    for up in UserProgress.objects.filter(user=user, is_completed=True, completed_at__isnull=False).select_related('topic', 'topic__course').order_by('-completed_at')[:10]:
        activities.append({
            'type': 'topic',
            'icon': 'fa-solid fa-book-open',
            'color': 'text-brand-500',
            'bg': 'bg-blue-50',
            'text': f'Completed "{up.topic.title}"',
            'sub': up.topic.course.title,
            'time': up.completed_at,
        })
    activities.sort(key=lambda a: a['time'], reverse=True)
    recent_activities = activities[:8]

    return render(request, 'users/profile.html', {
        'profile':            profile,
        'course_data':        course_data,
        'total_topics_done':  total_topics_done,
        'courses_started':    courses_started,
        'courses_completed':  courses_completed,
        'user_achievements':  user_achievements,
        'streak':             streak,
        'xp_level':           xp_level,
        'xp_in_level':        xp_in_level,
        'xp_per_level':       xp_per_level,
        'xp_pct':             xp_pct,
        'recent_activities':  recent_activities,
        'heatmap_json':       heatmap_json,
        'total_active_days':  total_active_days,
        'top_points':         top_points,
        'status_choices':     UserProfile.STATUS_CHOICES,
    })
