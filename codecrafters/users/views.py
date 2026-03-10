from django.shortcuts import render

def login_view(request):
    """
    Renders the custom Gamified Login page.
    """
    return render(request, 'users/login.html')

def register_view(request):
    """
    Renders the custom Gamified Registration page.
    """
    return render(request, 'users/register.html')
