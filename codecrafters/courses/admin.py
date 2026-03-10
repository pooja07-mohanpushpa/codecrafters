from django.contrib import admin
from .models import Course, Topic, UserProgress, Achievement, UserAchievement


class TopicInline(admin.TabularInline):
    model  = Topic
    extra  = 1
    fields = ('title', 'order', 'points_reward', 'video_url')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ('title', 'total_topics', 'points_available', 'order')
    search_fields = ('title',)
    inlines       = [TopicInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display  = ('title', 'course', 'order', 'points_reward')
    list_filter   = ('course',)
    search_fields = ('title',)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display  = ('user', 'topic', 'is_completed', 'quiz_score', 'completed_at')
    list_filter   = ('is_completed', 'topic__course')
    search_fields = ('user__username',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'requirement_type', 'requirement_value')


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'unlocked_at')
