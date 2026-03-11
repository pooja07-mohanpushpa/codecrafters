import os
import django
import uuid
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Course, Topic, UserProgress, CourseProgress, Certificate, Achievement, UserAchievement
from users.models import UserProfile

def setup_demo_admin():
    try:
        admin_user = User.objects.get(username='admin')
        python_course = Course.objects.filter(title__icontains='Python').first()
        
        if not python_course:
            print("Python course not found.")
            return

        # 1. Update Course Progress to 90%
        cp, created = CourseProgress.objects.get_or_create(user=admin_user, course=python_course)
        total_topics = python_course.topics.count()
        # We'll set it to exactly 90%
        cp.progress_percentage = 90.0
        # Assume 9 out of 10 or similar; let's just force the number
        cp.topics_completed = int(total_topics * 0.9)
        cp.stars_earned = 4 # 90% / 20%
        cp.save()
        
        # 2. Ensure some topics are marked completed to match the percentage
        topics = python_course.topics.all().order_by('order')
        for i in range(cp.topics_completed):
            topic = topics[i]
            up, _ = UserProgress.objects.get_or_create(user=admin_user, topic=topic)
            up.is_completed = True
            up.quiz_score = 5
            up.highest_quiz_score = 5
            if not up.completed_at:
                up.completed_at = timezone.now()
            up.save()

        # 3. Generate Certificate (even at 90% for demo purpose as requested)
        cert, cert_created = Certificate.objects.get_or_create(
            user=admin_user, 
            course=python_course,
            defaults={'certificate_id': uuid.uuid4()}
        )
        if cert_created:
            print(f"Certificate generated for {admin_user.username} in {python_course.title}")
        else:
            print(f"Certificate already exists for {admin_user.username}")

        # 4. Give a Badge (Achievement)
        badge, _ = Achievement.objects.get_or_create(
            name="Python Elite",
            defaults={
                "description": "Mastered 90% of the Python technical track.",
                "requirement_type": "course",
                "requirement_value": 90
            }
        )
        ua, ua_created = UserAchievement.objects.get_or_create(user=admin_user, achievement=badge)
        if ua_created:
            print(f"Badge 'Python Elite' granted to {admin_user.username}")
        
        # 5. Update Profile Points for the flex
        profile = admin_user.profile
        profile.code_points += 450
        profile.save()

        print(f"Successfully updated {admin_user.username} to 90% completion in {python_course.title}")

    except User.DoesNotExist:
        print("User 'admin' does not exist. Please register first.")

if __name__ == '__main__':
    setup_demo_admin()
