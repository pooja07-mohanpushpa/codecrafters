import os
import django
from django.core.files.base import ContentFile
from io import BytesIO
from reportlab.pdfgen import canvas

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import UserProfile
from courses.models import Course, Certificate

# Create Jenny
j_user, created = User.objects.get_or_create(username='jenny')
if created:
    j_user.set_password('pass123')
    j_user.save()
j_prof = j_user.profile
j_prof.code_points = 1250
j_prof.challenges_solved = 15
j_prof.linkedin_url = 'https://www.linkedin.com/in/jenny-coder-demo/'
j_prof.save()

# Create Mike
m_user, created = User.objects.get_or_create(username='mike')
if created:
    m_user.set_password('pass123')
    m_user.save()
m_prof = m_user.profile
m_prof.code_points = 800
m_prof.challenges_solved = 8
m_prof.linkedin_url = 'https://www.linkedin.com/in/mike-dev-demo/'
m_prof.save()

py_course = Course.objects.filter(title__icontains='Python').first()
c_course = Course.objects.filter(title__icontains='C').first()

if py_course and not Certificate.objects.filter(user=j_user, course=py_course).exists():
    Certificate.objects.create(user=j_user, course=py_course)
    print("Jenny earned Python cert!")

if c_course and not Certificate.objects.filter(user=m_user, course=c_course).exists():
    Certificate.objects.create(user=m_user, course=c_course)
    print("Mike earned C cert!")

print('Demo users Jenny and Mike updated with certificates and points!')
