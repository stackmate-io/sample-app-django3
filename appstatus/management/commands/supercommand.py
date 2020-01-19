from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Builds the application'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Successfully ran the SUPER command'))
