import csv
import os
from django.core.management.base import BaseCommand, CommandError, CommandParser

from ...models import Professor, Subject, Faculty, Career, StudyPlan, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester, TimePeriod, CarmenTable
from ...serializers import ProfessorSerializer, SubjectSerializer, FacultySerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ScientificDegreeSerializer, TeachingCategorySerializer, ClassTypeSerializer, SemesterSerializer, TimePeriodSerializer, CarmenTableSerializer
from ...serializers_csv import CareerSerializerCSV, CarmenTableSerializerCSV, ClassTypeSerializerCSV, DepartmentSerializerCSV, FacultySerializerCSV, ProfessorSerializerCSV, ScientificDegreeSerializerCSV, SemesterSerializerCSV, StudyPlanSerializerCSV, SubjectSerializerCSV, TeachingCategorySerializerCSV, TeachingGroupSerializerCSV, TimePeriodSerializerCSV


CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')
PROFESSOR_DIR = os.path.join(CURRENT_PATH, '../../excels/professors.csv')
FACULTY_DIR = os.path.join(CURRENT_PATH, '../../excels/faculties.csv')
CAREER_DIR = os.path.join(CURRENT_PATH, '../../excels/careers.csv')
STUDY_PLAN_DIR = os.path.join(CURRENT_PATH, '../../excels/study_plans.csv')
DEPARTMENT_DIR = os.path.join(CURRENT_PATH, '../../excels/departments.csv')
SEMESTER_DIR = os.path.join(CURRENT_PATH, '../../excels/semesters.csv')
CLASS_TYPE_DIR = os.path.join(CURRENT_PATH, '../../excels/class_types.csv')
TIME_PERIOD_DIR = os.path.join(CURRENT_PATH, '../../excels/time_periods.csv')
CARMEN_TABLE_DIR = os.path.join(CURRENT_PATH, '../../excels/carmen_table.csv')
TEACHING_GROUP_DIR = os.path.join(
    CURRENT_PATH, '../../excels/teaching_groups.csv')
TEACHING_CATEGORY_DIR = os.path.join(
    CURRENT_PATH, '../../excels/teaching_categories.csv')
SCIENTIFIC_DEGREE_DIR = os.path.join(
    CURRENT_PATH, '../../excels/scientific_degrees.csv')


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('-m', '--model', type=str)

    def handle(self, *args, **options):
        model_name = options['model'] if options['model'] else 'All'

        fieldnames, data, file_path = self.get_fieldnames_and_data(model_name)

        with open(file_path, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def get_fieldnames_and_data(self, name: str):
        if name == 'Subjects':
            queryset = Subject.objects.all()
            fieldnames = ['name', 'department', 'career',
                          'study_plan', 'semester', 'number_of_hours']
            data = [SubjectSerializerCSV(subject).data for subject in queryset]
            file_path = SUBJECTS_DIR

        elif name == 'Professors':
            queryset = Professor.objects.all()
            fieldnames = ['name', 'last_name', 'department', 'scientific_degree',
                          'teaching_category', 'faculty']
            data = [ProfessorSerializerCSV(
                professor).data for professor in queryset]
            file_path = PROFESSOR_DIR

        elif name == 'Faculties':
            queryset = Faculty.objects.all()
            fieldnames = ['name', ]
            data = [FacultySerializerCSV(faculty).data for faculty in queryset]
            file_path = FACULTY_DIR

        elif name == 'Careers':
            queryset = Career.objects.all()
            fieldnames = ['name', 'faculty']
            data = [CareerSerializerCSV(career).data for career in queryset]
            file_path = CAREER_DIR

        elif name == 'StudyPlans':
            queryset = StudyPlan.objects.all()
            fieldnames = ['name',
                          'number_of_semesters', 'until', 'since']
            data = [StudyPlanSerializerCSV(
                study_plan).data for study_plan in queryset]
            file_path = STUDY_PLAN_DIR

        elif name == 'TeachingGroups':
            queryset = TeachingGroup.objects.all()
            fieldnames = ['name']
            data = [TeachingGroupSerializerCSV(
                teaching_group).data for teaching_group in queryset]
            file_path = TEACHING_GROUP_DIR

        elif name == 'Departments':
            queryset = Department.objects.all()
            fieldnames = ['name', 'faculty']
            data = [DepartmentSerializerCSV(
                dapartment).data for dapartment in queryset]
            file_path = DEPARTMENT_DIR

        elif name == 'ScientificDegrees':
            queryset = ScientificDegree.objects.all()
            fieldnames = ['name']
            data = [ScientificDegreeSerializerCSV(
                scientific_degree).data for scientific_degree in queryset]
            file_path = SCIENTIFIC_DEGREE_DIR

        elif name == 'TeachingCategories':
            queryset = TeachingCategory.objects.all()
            fieldnames = ['name']
            data = [TeachingCategorySerializerCSV(
                teaching_category).data for teaching_category in queryset]
            file_path = TEACHING_CATEGORY_DIR

        elif name == 'Semesters':
            queryset = Semester.objects.all()
            fieldnames = ['name']
            data = [SemesterSerializerCSV(
                semester).data for semester in queryset]
            file_path = SEMESTER_DIR

        elif name == 'ClassTypes':
            queryset = ClassType.objects.all()
            fieldnames = ['name']
            data = [ClassTypeSerializerCSV(
                class_type).data for class_type in queryset]
            file_path = CLASS_TYPE_DIR

        elif name == 'TimePeriods':
            queryset = TimePeriod.objects.all()
            fieldnames = ['name']
            data = [TimePeriodSerializerCSV(
                time_period).data for time_period in queryset]
            file_path = TIME_PERIOD_DIR

        elif name == 'CarmenTable':
            queryset = CarmenTable.objects.all()
            fieldnames = ['teaching_group',
                          'study_plan', 'semester', 'time_period']
            data = [CarmenTableSerializerCSV(
                carmen_table).data for carmen_table in queryset]
            file_path = CARMEN_TABLE_DIR

        else:
            print("error")

        return fieldnames, data, file_path
