"""
Context processor: injects the logged-in user's UserProfile into every template.
This allows the navbar to show real PathPoints without touching individual views.
"""
from users.models import UserProfile


def user_profile(request):
    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        return {'profile': profile}
    return {'profile': None}
