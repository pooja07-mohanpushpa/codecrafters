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
    User profile panel — shows stats, course progress, and account settings.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    all_courses = Course.objects.prefetch_related('topics').order_by('order')
    course_data = []
    for course in all_courses:
        total = course.topics.count()
        done  = UserProgress.objects.filter(user=user, topic__course=course, is_completed=True).count()
        pct   = int((done / total) * 100) if total > 0 else 0
        stars = pct // 20
        course_data.append({
            'course':      course,
            'total':       total,
            'done':        done,
            'pct':         pct,
            'stars_range': range(stars),
            'empty_range': range(5 - stars),
        })

    return render(request, 'users/profile.html', {
        'profile':     profile,
        'course_data': course_data,
    })
