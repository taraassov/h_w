from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test1@mail.com',
            first_name='user',
            last_name='userov',
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password('qazwsx2020g2')
        user.save()
