import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course

def main():
    try:
        course = Course.objects.get(title="Python Masterclass")
    except Course.DoesNotExist:
        print("Course not found!")
        return

    for topic in course.topics.all():
        summary = (
            f"In this lesson, we cover {topic.title}. This discussion is designed "
            "to give you a strong fundamental understanding of the topic and how to apply it in your Python projects.\n\n"
            "Credits & Citation:\n"
            "The audio and video content for this lesson was generated using Google's NotebookLM. "
            "We thank Google and the NotebookLM team for providing the AI tools used to create these interactive learning experiences."
        )
        topic.content = summary
        topic.save()
        print(f"Updated: {topic.title}")

    print("All Python Masterclass topics have been updated with lesson summaries and citations.")

if __name__ == '__main__':
    main()
