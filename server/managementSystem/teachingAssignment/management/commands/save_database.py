import csv
import os
from django.core.management.base import BaseCommand, CommandError
from ...models import Subject
from ...serializers import SubjectSerializer

CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')


class Command(BaseCommand):
    help = 'Save database data in excels'

    def handle(self, *args, **options):
        # try:
        subjects = Subject.objects.all()

        fieldnames = ['id', 'name', 'department', 'career',
                      'study_plan', 'semester', 'number_of_hours']

        data = []
        for subject in subjects:
            subject = SubjectSerializer(subject).data
            data.append(subject)

        with open(SUBJECTS_DIR, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


    

        # except:
        #     raise CommandError("Something went wrong")
