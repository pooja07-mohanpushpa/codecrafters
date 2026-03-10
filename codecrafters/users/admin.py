from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'code_points', 'stars_earned', 'challenges_solved')
    search_fields = ('user__username', 'user__email')
    ordering      = ('-code_points',)
