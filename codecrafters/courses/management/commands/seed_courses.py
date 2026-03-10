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
        "points_available": 950,
        "order": 1,
        "topics": [
            ("Introduction",                              1, 50),
            ("Variables",                                  2, 50),
            ("Data Types",                                 3, 50),
            ("Type Casting",                               4, 50),
            ("Input and Output",                           5, 50),
            ("Arithmetic and Comparison Operators",        6, 50),
            ("Logical and Assignment Operators",           7, 50),
            ("Control Flow (if, elif, else)",              8, 50),
            ("Nested Conditions",                          9, 50),
            ("For Loops",                                 10, 50),
            ("While Loops",                               11, 50),
            ("Loop Control Statements (break, continue, pass)", 12, 50),
            ("Lists",                                     13, 50),
            ("Tuples",                                    14, 50),
            ("Sets",                                      15, 50),
            ("Dictionaries",                              16, 50),
            ("Functions",                                 17, 50),
            ("Strings",                                   18, 50),
            ("File Handling",                             19, 50),
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
    {
        "title": "Java Fundamentals",
        "description": "Learn object-oriented concepts, multithreading, and enterprise application development with Java.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg",
        "gradient_from": "from-orange-500",
        "gradient_to": "to-red-600",
        "points_available": 600,
        "order": 3,
        "topics": [
            ("Introduction to Java",       1, 60),
            ("Variables & Data Types",      2, 60),
            ("Control Flow",               3, 60),
            ("Classes & Objects",          4, 60),
            ("Inheritance & Polymorphism", 5, 60),
            ("Interfaces & Abstract Classes",6,60),
            ("Exception Handling",         7, 60),
            ("Collections Framework",      8, 60),
            ("Generics",                   9, 60),
            ("Multithreading",            10, 60),
        ],
    },
    {
        "title": "Modern JavaScript",
        "description": "Build dynamic web applications using DOM manipulation, Promises, and ES6+ features.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
        "gradient_from": "from-yellow-400",
        "gradient_to": "to-yellow-600",
        "points_available": 500,
        "order": 4,
        "topics": [
            ("Introduction & Syntax",      1, 50),
            ("Variables & Scoping",        2, 50),
            ("Functions & Arrow Functions",3, 50),
            ("Objects & Arrays",           4, 50),
            ("DOM Manipulation",           5, 50),
            ("Events & Listeners",         6, 50),
            ("Asynchronous JS (Callbacks)",7, 50),
            ("Promises & async/await",     8, 50),
            ("ES6+ Features",              9, 50),
            ("Modules & Tooling",         10, 50),
        ],
    },
    {
        "title": "C++ for Performance",
        "description": "Dive deep into memory management, STL, and high-performance system programming in C++.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg",
        "gradient_from": "from-blue-700",
        "gradient_to": "to-blue-900",
        "points_available": 700,
        "order": 5,
        "topics": [
            ("C++ Basics",                 1, 70),
            ("Control Structures",         2, 70),
            ("Pointers & References",      3, 70),
            ("Functions & Overloading",    4, 70),
            ("Classes & Object-Oriented",  5, 70),
            ("Constructors & Destructors", 6, 70),
            ("Inheritance & Polymorphism", 7, 70),
            ("Templates",                  8, 70),
            ("Standard Template Library",  9, 70),
            ("Memory Management",         10, 70),
        ],
    },
    {
        "title": "Go Programming",
        "description": "Master concurrency and build scalable backend services with Google's Go language.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg",
        "gradient_from": "from-cyan-400",
        "gradient_to": "to-blue-500",
        "points_available": 600,
        "order": 6,
        "topics": [
            ("Getting Started with Go",    1, 60),
            ("Variables & Data Types",     2, 60),
            ("Control Structures",          3, 60),
            ("Arrays, Slices & Maps",      4, 60),
            ("Functions & Pointers",       5, 60),
            ("Structs & Methods",          6, 60),
            ("Interfaces",                 7, 60),
            ("Error Handling",             8, 60),
            ("Goroutines & Channels",      9, 60),
            ("Building a Web API",        10, 60),
        ],
    },
    {
        "title": "Rust Programming",
        "description": "Learn memory safety, lifetimes, and zero-cost abstractions with Rust.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg",
        "gradient_from": "from-stone-700",
        "gradient_to": "to-stone-900",
        "points_available": 800,
        "order": 7,
        "topics": [
            ("Introduction to Rust",       1, 80),
            ("Variables & Mutability",      2, 80),
            ("Data Types & Functions",     3, 80),
            ("Control Flow",               4, 80),
            ("Ownership & Borrowing",      5, 80),
            ("Structs & Enums",            6, 80),
            ("Pattern Matching",           7, 80),
            ("Modules & Crates",           8, 80),
            ("Collections",                9, 80),
            ("Error Handling",            10, 80),
        ],
    },
    {
        "title": "Ruby Basics",
        "description": "Enjoy programmer happiness while building web applications with Ruby.",
        "icon_url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/ruby/ruby-original.svg",
        "gradient_from": "from-red-500",
        "gradient_to": "to-red-700",
        "points_available": 500,
        "order": 8,
        "topics": [
            ("Introduction to Ruby",       1, 50),
            ("Variables & Methods",         2, 50),
            ("Control Flow",               3, 50),
            ("Arrays & Hashes",            4, 50),
            ("Blocks & Iterators",         5, 50),
            ("Classes & Objects",          6, 50),
            ("Modules & Mixins",           7, 50),
            ("Exception Handling",         8, 50),
            ("File I/O",                   9, 50),
            ("Regular Expressions",       10, 50),
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

        self.stdout.write(self.style.SUCCESS("Courses seeded successfully!"))
