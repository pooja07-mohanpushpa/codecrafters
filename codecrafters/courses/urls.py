from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('courses/', views.courses_view, name='courses'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('topic/<int:topic_id>/', views.topic_detail_view, name='topic_detail'),
    path('quiz/generate/<int:topic_id>/', views.generate_quiz, name='generate_quiz'),
    path('quiz/submit/<int:topic_id>/', views.submit_quiz, name='submit_quiz'),
    path('certificate/<uuid:certificate_id>/download/', views.download_certificate, name='download_certificate'),
    path('rewards/', views.rewards_view, name='rewards'),
]

