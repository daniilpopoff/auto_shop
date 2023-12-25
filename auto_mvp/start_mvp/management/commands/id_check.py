from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Your command description here'

    def handle(self, *args, **options):
        # Replace 'your_username' with the actual username you want to check
        username = 'qwerty'

        # Retrieve the user instance
        user = get_user_model()
        user = user.objects.get(username=username)

        # Access the user's ID
        user_id = user.id

        # Print the user's ID to the console
        self.stdout.write(self.style.SUCCESS(f"User ID for {username}: {user_id}"))