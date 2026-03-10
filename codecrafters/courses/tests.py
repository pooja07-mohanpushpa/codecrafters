from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Course, Topic, Achievement, UserAchievement
from users.models import UserProfile

class DashboardTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.course = Course.objects.create(title='Test Course', order=1)
        self.topic = Topic.objects.create(course=self.course, title='Test Topic', order=1, points_reward=50)
        self.achievement = Achievement.objects.create(name='Test Achievement', description='Testing', requirement_type='points', requirement_value=10)

    def test_dashboard_access(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/dashboard.html')

    def test_course_detail_access(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(f'/dashboard/course/{self.course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_achievements_display(self):
        # Assign achievement
        UserAchievement.objects.create(user=self.user, achievement=self.achievement)
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/dashboard/')
        self.assertContains(response, 'Test Achievement')

    def test_arena_access(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/dashboard/arena/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/arena.html')
