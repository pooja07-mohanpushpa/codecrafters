import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

# Map a,b,c,d to 0,1,2,3
ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

# The user's exact answer key structure
answer_key = {
    "Introduction": ['b', 'b', 'b', 'b', 'b'],
    "Variables": ['b', 'b', 'c', 'b', 'b'],
    "Data Types": ['a', 'c', 'c', 'a', 'b'],
    "Type Casting": ['a', 'b', 'b', 'a', 'a'],
    "Input and Output": ['c', 'c', 'c', 'b', 'b'],
    "Arithmetic and Comparison Operators": ['a', 'b', 'b', 'b', 'a'],
    "Logical and Assignment Operators": ['b', 'a', 'b', 'b', 'a'],
    "Control Flow (if, elif, else)": ['b', 'a', 'b', 'b', 'a'],
    "Nested Conditions": ['a', 'a', 'd', 'b', 'c'],
    "For Loops": ['b', 'b', 'a', 'b', 'b'],
    "While Loops": ['b', 'c', 'b', 'b', 'a'],
    "Loop Control Statements": ['b', 'b', 'b', 'a', 'a'], # Note title mismatch mitigation below
    "Lists": ['b', 'b', 'b', 'b', 'b'],
    "Tuples": ['c', 'b', 'b', 'b', 'b'],
    "Sets": ['c', 'b', 'b', 'b', 'b'],
    "Dictionaries": ['b', 'b', 'b', 'a', 'a'],
    "Functions": ['c', 'd', 'b', 'c', 'a'],
    "Strings": ['a', 'b', 'a', 'a', 'd'],
    "File Handling": ['a', 'b', 'a', 'c', 'a']
}

updated_count = 0

for key_title, answers in answer_key.items():
    # Fuzzy match the title because "Loop Control Statements" in key 
    # maps to "Loop Control Statements (break, continue, pass)" in DB
    topic = Topic.objects.filter(title__icontains=key_title, course__title='Python Masterclass').first()
    
    if topic and topic.predefined_quiz:
        quiz_data = topic.predefined_quiz
        
        # Update each question's correct index based on the map
        for i, q in enumerate(quiz_data):
            if i < len(answers):
                q['correct'] = ans_map[answers[i]]
        
        topic.predefined_quiz = quiz_data
        topic.save()
        updated_count += 1
        print(f"Applied perfect answer key to: {topic.title}")

print(f"\nSuccessfully strictly mapped answer keys for {updated_count} topics!")
