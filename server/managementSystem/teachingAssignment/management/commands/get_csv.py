import os
import csv
from ...serializers import ProfessorSerializer, SubjectSerializer, FacultySerializer, CareerSerializer, StudyPlanSerializer, TeachingAssignmentSerializer, TeachingGroupSerializer, DepartmentSerializer, ScientificDegreeSerializer, TeachingCategorySerializer, ClassTypeSerializer, SemesterSerializer, TimePeriodSerializer, CarmenTableSerializer
from ...models import Professor, Subject, Faculty, Career, StudyPlan, TeachingAssignment, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester, TimePeriod, CarmenTable
from django.core.management.base import BaseCommand, CommandError, CommandParser

# my data rows as dictionary objects
mydict = [
    {
        'Facultad': 'COE',
        'Tipo curso': '9.0',
        'Año': 'Nikhil',
        'Asignatura': '2',
        'Horas': '4',
        'G': '1/3',
        'Profesor': 'Pepe'
    }
]

# field names
fields = ['Facultad', 'Tipo curso', 'Año',
          'Asignatura', 'Horas', 'G', 'Profesor']

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)


CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')


class Command(BaseCommand):
    help = 'Create a csv file with the Teaching Assignments'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('department_name', type=str)

    def handle(self, *args, **options):
        # department_name = 'Matemática Aplicada'
        department_name = options['department_name']
        data = self.filter_by_department(department_name)

        fieldnames = ['Facultad', 'Tipo curso', 'Año',
                      'Asignatura', 'Horas', 'G', 'Profesor']

        print(data)

        # with open(file_path, 'w', encoding='UTF8') as f:
        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerows(data)

    def filter_by_department(self, department_name):
        queryset = TeachingAssignment.objects.all()
        data = [
            TeachingAssignmentSerializer(teachingAssignment).data
            for teachingAssignment in queryset]
        data = [
            teaching_assignment for teaching_assignment in data
            if teaching_assignment['subject_description']['department'] == department_name]

        return data
