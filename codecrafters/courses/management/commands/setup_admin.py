"""
One-time management command to create/update the admin superuser with a known password.
Run: python manage.py setup_admin
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile


class Command(BaseCommand):
    help = "Creates or updates the admin superuser with preset credentials."

    def handle(self, *args, **kwargs):
        username = "admin"
        password = "Admin@123"
        email    = "admin@pathmind.com"

        user, created = User.objects.get_or_create(username=username)
        user.email        = email
        user.is_staff     = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        UserProfile.objects.get_or_create(user=user)

        action = "Created" if created else "Updated"
        self.stdout.write(f"{action} admin account.")
        self.stdout.write(f"  Username : {username}")
        self.stdout.write(f"  Password : {password}")
        self.stdout.write(f"  URL      : http://127.0.0.1:8000/admin/")
