from django.contrib import admin
from .models import CodingProblem, TestCase, UserSubmission

class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1

@admin.register(CodingProblem)
class CodingProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'points_reward', 'order')
    list_filter = ('difficulty',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TestCaseInline]

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'language', 'status', 'submitted_at')
    list_filter = ('status', 'language')
    readonly_fields = ('submitted_at',)
