import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathmind.settings')
django.setup()

from django.contrib.auth import get_user_model
from courses.models import Course, Topic, UserProgress, Certificate

User = get_user_model()

def generate_demo_user():
    # 1. Create or get Demo User
    user, created = User.objects.get_or_create(username='demouser', defaults={
        'email': 'demo@pathmind.com',
        'first_name': 'Demo',
        'last_name': 'Student'
    })
    if created:
        user.set_password('demo1234')
        user.save()
        print("Created demo user 'demouser' with password 'demo1234'")
    else:
        print("Demo user 'demouser' already exists.")

    # 2. Get the target course (e.g., Python Masterclass)
    course = Course.objects.filter(title__icontains="Python").first()
    if not course:
        print("No Python course found. Creating a dummy course.")
        course = Course.objects.create(
            title="Python Masterclass",
            description="Master Python from scratch.",
            total_topics=2,
            points_available=100
        )
        t1 = Topic.objects.create(course=course, title="Intro to Python", order=1, points_reward=50)
        t2 = Topic.objects.create(course=course, title="Advanced Python", order=2, points_reward=50)
    else:
        print(f"Found course: {course.title}")

    # 3. Mark all topics in the course as completed for the demo user
    topics = course.topics.all()
    for topic in topics:
        progress, p_created = UserProgress.objects.get_or_create(user=user, topic=topic)
        if not progress.is_completed:
            progress.is_completed = True
            progress.highest_quiz_score = 5
            progress.save()
            print(f"Marked topic '{topic.title}' as completed.")
        
    # 4. Generate Certificate
    cert, c_created = Certificate.objects.get_or_create(user=user, course=course)
    if c_created:
        print(f"Generated Certificate {cert.certificate_id} for {user.username} in {course.title}")
    else:
        print(f"Certificate already exists for {user.username} in {course.title}: {cert.certificate_id}")

if __name__ == '__main__':
    generate_demo_user()
