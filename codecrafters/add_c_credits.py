import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

credits_text = """

Credits & Citation:
The audio and video content for this lesson was generated using Google's NotebookLM. We thank Google and the NotebookLM team for providing the AI tools used to create these interactive learning experiences."""

topics = Topic.objects.filter(course__title='C Programming')
count = 0
for t in topics:
    if credits_text not in t.content:
        t.content = t.content.strip() + credits_text
        t.save()
        count += 1

print(f'Successfully added credits to {count} C Programming topics.')
