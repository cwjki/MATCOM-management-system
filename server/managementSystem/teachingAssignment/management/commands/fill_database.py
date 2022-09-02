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

        if model_name == 'All':
            self.fill_all()
        else:
            self.fill_model(model_name)

    def fill_all(self):
        print('All')
        pass

    def fill_model(self, model_name: str):
        print(model_name)
        pass
