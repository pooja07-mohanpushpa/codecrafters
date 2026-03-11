from courses.models import Topic
import json

topic = Topic.objects.filter(title='For Loops', course__title='Python Masterclass').first()
if topic:
    quiz = [
        {
            "id": 1,
            "question": "Which of the following is the correct syntax for a for loop in Python?",
            "options": ["for i in range(5):", "for (i=0; i<5; i++)", "for i from 1 to 5:", "foreach i in list:"],
            "correct": 0
        },
        {
            "id": 2,
            "question": "What does the range(5) function generate in a for loop?",
            "options": ["A list of 5 random numbers", "Numbers from 1 to 5", "Numbers from 0 to 4", "Numbers from 0 to 5"],
            "correct": 2
        },
        {
            "id": 3,
            "question": "How do you iterate over both the index and the value of a list in a for loop?",
            "options": ["Using enumerate()", "Using range(len(list))", "Using zip()", "Using list.items()"],
            "correct": 0
        },
        {
            "id": 4,
            "question": "What is the purpose of the 'else' clause in a Python for loop?",
            "options": ["It runs if the loop is broken by 'break'", "It runs after the loop finishes normally (without break)", "It runs on every iteration", "It is not a valid syntax for loops"],
            "correct": 1
        },
        {
            "id": 5,
            "question": "How can you exit a for loop prematurely?",
            "options": ["exit", "stop", "break", "continue"],
            "correct": 2
        }
    ]
    topic.predefined_quiz = quiz
    topic.save()
    print("Successfully seeded quiz for 'For Loops'")
else:
    print("Topic 'For Loops' not found")
