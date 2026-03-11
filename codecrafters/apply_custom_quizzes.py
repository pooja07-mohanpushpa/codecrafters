import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

with open('user_quizzes.json', 'r') as f:
    custom_quizzes = json.load(f)

updated_count = 0
for topic_title, qs in custom_quizzes.items():
    topic = Topic.objects.filter(title=topic_title, course__title='Python Masterclass').first()
    if topic:
        formatted_quiz = []
        for i, q in enumerate(qs, start=1):
            
            # Find the correct index
            try:
                correct_idx = q['options'].index(q['answer'])
            except ValueError:
                # If the explicit answer isn't in the options array exactly, default to 0
                correct_idx = 0
                
            formatted_quiz.append({
                "id": i,
                "question": q['question'],
                "options": q['options'],
                "correct": correct_idx
            })
            
        topic.predefined_quiz = formatted_quiz
        topic.save()
        updated_count += 1
        print(f"Updated customized quiz for: {topic.title}")

print(f"\nSuccessfully overwrote {updated_count} topics with custom user quizzes!")
