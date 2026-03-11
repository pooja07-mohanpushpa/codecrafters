import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

topics = Topic.objects.filter(course__title='Python Masterclass').order_by('order')
inconsistencies = []

for t in topics:
    quiz = t.predefined_quiz
    if not quiz:
        inconsistencies.append(f"{t.title}: No quiz found!")
        continue
    
    if len(quiz) != 5:
        inconsistencies.append(f"{t.title}: Has {len(quiz)} questions, expected 5")
        
    for q in quiz:
        options = q.get('options', [])
        if len(options) != 4:
            inconsistencies.append(f"{t.title} Q{q.get('id')}: Has {len(options)} options, expected 4")
        
        correct_idx = q.get('correct')
        if correct_idx not in [0, 1, 2, 3]:
            inconsistencies.append(f"{t.title} Q{q.get('id')}: Invalid correct index '{correct_idx}'")

if inconsistencies:
    print("WARNING: Inconsistencies found in the database:")
    for inc in inconsistencies:
        print(f"  - {inc}")
else:
    print("SUCCESS: Backend is 100% consistent!")
    print("Every topic has exactly 5 questions, 4 options each, and valid answer indices.")
