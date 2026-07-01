"""Create (or update) the admin superuser from ADMIN_* environment variables.

Set these in your .env, then run `python manage.py createadmin` (deploy.sh runs
it automatically). Credentials live in .env — never committed to git.

    ADMIN_USERNAME=admin
    ADMIN_EMAIL=you@example.com
    ADMIN_PASSWORD=YourStrongPassword
"""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the admin superuser from ADMIN_* environment variables."

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("ADMIN_USERNAME", "admin").strip()
        email = os.getenv("ADMIN_EMAIL", "").strip()
        password = os.getenv("ADMIN_PASSWORD", "")

        if not password:
            self.stdout.write("ADMIN_PASSWORD not set — skipping admin creation.")
            return

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        if email:
            user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        verb = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{verb} admin superuser '{username}'."))
