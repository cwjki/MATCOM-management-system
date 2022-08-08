import csv
import os
from pyexpat import model
from django.core.management.base import BaseCommand, CommandError, CommandParser
from ...models import Subject
from ...serializers import SubjectSerializer

CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        model_name = options['model_name']
        try:
            fieldnames, data = self.get_fieldnames_and_data(model_name)

            with open(SUBJECTS_DIR, 'w', encoding='UTF8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except:
            raise CommandError("Something went wrong")

    def get_fieldnames_and_data(self, name: str):
        if name == 'Subjects':
            queryset = Subject.objects.all()
            fieldnames = ['id', 'name', 'department', 'career',
                          'study_plan', 'semester', 'number_of_hours']
            data = [SubjectSerializer(subject).data for subject in queryset]

        else:
            print("error")

        return fieldnames, data
