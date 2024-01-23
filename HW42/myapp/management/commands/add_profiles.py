from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for existing users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f'Profile created for user {user.username}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Profile already exists for user {user.username}'))

# Login: admin13
# # Password: 654321