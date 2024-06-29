from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handdle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='admin',
            last_name='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123123123')
        user.save()
