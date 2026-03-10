"""
Management command to seed initial courses and topics into the database.
Run: python manage.py seed_courses
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Topic


COURSES = [
    {
        "title": "Python Masterclass",
        "description": "Learn Python from scratch — variables, loops, functions, and OOP with interactive AI video sessions.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
        "gradient_from": "from-blue-500",
        "gradient_to": "to-indigo-700",
        "points_available": 500,
        "order": 1,
        "topics": [
            ("Introduction to Python",      1, 50),
            ("Variables & Data Types",       2, 50),
            ("Operators & Expressions",      3, 50),
            ("Control Flow (if/else)",       4, 50),
            ("Loops (for & while)",          5, 50),
            ("Functions",                    6, 50),
            ("Lists & Tuples",               7, 50),
            ("Dictionaries & Sets",          8, 50),
            ("File I/O",                     9, 50),
            ("Object-Oriented Programming", 10, 50),
        ],
    },
    {
        "title": "C Foundations",
        "description": "Master memory management, pointers, and performance optimization with C programming.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg",
        "gradient_from": "from-slate-700",
        "gradient_to": "to-slate-900",
        "points_available": 600,
        "order": 2,
        "topics": [
            ("Introduction to C",          1, 50),
            ("Variables & Data Types",      2, 50),
            ("Operators",                   3, 50),
            ("Control Flow",               4, 50),
            ("Loops",                       5, 50),
            ("Functions & Scope",          6, 50),
            ("Arrays",                     7, 50),
            ("Strings",                    8, 50),
            ("Pointers",                   9, 50),
            ("Structs",                   10, 50),
            ("File I/O",                  11, 50),
            ("Memory Management",         12, 50),
        ],
    },
]


class Command(BaseCommand):
    help = "Seeds initial courses and topics into the database."

    def handle(self, *args, **kwargs):
        for course_data in COURSES:
            topics_data = course_data.pop("topics")
            course, created = Course.objects.get_or_create(
                title=course_data["title"],
                defaults=course_data,
            )
            action = "Created" if created else "Already exists"
            self.stdout.write(f"{action}: {course.title}")

            for title, order, pts in topics_data:
                Topic.objects.get_or_create(
                    course=course,
                    title=title,
                    defaults={"order": order, "points_reward": pts},
                )

        self.stdout.write(self.style.SUCCESS("✅ Courses seeded successfully!"))
