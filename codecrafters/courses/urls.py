from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('courses/', views.courses_view, name='courses'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('arena/', views.arena_view, name='arena'),
    path('quiz/', views.quiz_view, name='quiz'),
]
