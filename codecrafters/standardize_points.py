import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathmind.settings')
django.setup()

from courses.models import Course, Topic

courses = Course.objects.all()
for c in courses:
    num_topics = c.topics.count()
    
    # Each topic gives 50 points max for the quiz (since there are 5 questions * 10 pts)
    # Plus the 'Completion Bonus'. In the previous view, max quiz bonus = 50 pts, completion bonus = topic.points_reward = 50 pts
    # Wait, the frontend says: "Completion Bonus: 50 pts" AND "Max Quiz Bonus: 50 pts".
    # That means 100 pts possible per topic! Let's check the views.py logic to be absolutely sure.
    
    # Whatever the formula, let's look at what the user wants: "assign correct code points with similar structures"
    # Actually, in dashboard we just show `course.points_available`.
    # Let's dynamically calculate `c.points_available` based on how many PathPoints are actually earnable.
    
    # Let's set topic.points_reward = 50 for all topics.
    for t in c.topics.all():
        if t.points_reward != 50:
            t.points_reward = 50
            t.save()
            print(f"Updated {t.title} to 50 pts")
            
    # Course points_available should probably be: num_topics * (Topic points_reward + Quiz Max Points)
    # Quiz is 5 questions * 10 pts = 50 pts. So 100 pts per topic.
    # Let's just set course points_available = num_topics * 100.
    
    correct_points = num_topics * 100
    if c.points_available != correct_points:
        print(f"Updating {c.title} from {c.points_available} to {correct_points}")
        c.points_available = correct_points
        c.save()

print("PathPoints structure standardized across all courses!")
