from ast import Raise
from django.core.management.base import BaseCommand, CommandError, CommandParser
from ...models import Subject


class Command(BaseCommand):
    help = 'Save database data in excels'

    def handle(self, *args, **options):
        try:
            subjects = Subject.objects.all()

        except:
            raise CommandError("Something went wrong")
