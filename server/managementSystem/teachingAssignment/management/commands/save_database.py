import csv
from importlib.resources import path
import os
from pyexpat import model
from django.core.management.base import BaseCommand, CommandError, CommandParser
from ...models import Professor, Subject
from ...serializers import ProfessorSerializer, SubjectSerializer

CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')
PROFESSOR_DIR = os.path.join(CURRENT_PATH, '../../excels/professors.csv')


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        model_name = options['model_name']
        # try:
        fieldnames, data, path = self.get_fieldnames_and_data(model_name)

        with open(path, 'w', encoding='UTF8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        # except:
            # raise CommandError("Something went wrong")

    def get_fieldnames_and_data(self, name: str):
        if name == 'Subjects':
            queryset = Subject.objects.all()
            fieldnames = ['id', 'name', 'department', 'career',
                          'study_plan', 'semester', 'number_of_hours']
            data = [SubjectSerializer(subject).data for subject in queryset]
            path = SUBJECTS_DIR

        elif name == 'Professors':
            queryset = Professor.objects.all()
            fieldnames = ['id', 'name', 'last_name', 'department', 'scientific_degree',
                          'teaching_category', 'faculty']
            data = [ProfessorSerializer(
                professor).data for professor in queryset]
            path = PROFESSOR_DIR

        else:
            print("error")

        return fieldnames, data, path
