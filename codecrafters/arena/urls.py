from django.urls import path
from . import views

urlpatterns = [
    path('', views.arena_home, name='arena_home'),
    path('problem/<slug:slug>/', views.problem_detail, name='arena_problem'),
    path('submit/', views.submit_code, name='arena_submit'),
]
