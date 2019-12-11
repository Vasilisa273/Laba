from django.core.management import BaseCommand

from polls.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@localhost.localdomain', 'admin')
