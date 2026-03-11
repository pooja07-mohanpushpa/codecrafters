import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

topics = Topic.objects.filter(course__title='C Programming').order_by('order')

out_file = "courses/management/commands/seed_c_quizzes.py"

with open(out_file, "w", encoding="utf-8") as f:
    f.write("from django.core.management.base import BaseCommand\n")
    f.write("from courses.models import Topic\n\n")
    f.write("class Command(BaseCommand):\n")
    f.write("    help = 'Seeds 19 Quizzes for the C Programming Course'\n\n")
    f.write("    def handle(self, *args, **options):\n")
    f.write("        quizzes = {\n")
    
    for t in topics:
        if t.predefined_quiz:
            f.write(f'            "{t.title}": ')
            json.dump(t.predefined_quiz, f, indent=4)
            f.write(',\n')
        
    f.write("        }\n\n")
    f.write("        count = 0\n")
    f.write("        for title, quiz in quizzes.items():\n")
    f.write("            topic = Topic.objects.filter(title=title, course__title='C Programming').first()\n")
    f.write("            if topic:\n")
    f.write("                topic.predefined_quiz = quiz\n")
    f.write("                topic.save()\n")
    f.write("                count += 1\n\n")
    f.write("        self.stdout.write(self.style.SUCCESS(f'Successfully re-seeded {count} C Programming quizzes!'))\n")

print(f"Generated {out_file}")
