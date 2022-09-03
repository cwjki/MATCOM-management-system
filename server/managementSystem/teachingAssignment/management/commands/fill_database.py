import csv
import os
from django.core.management.base import BaseCommand, CommandError, CommandParser

from ...models import Professor, Subject, Faculty, Career, StudyPlan, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester, TimePeriod, CarmenTable
from ...serializers import ProfessorSerializer, SubjectSerializer, FacultySerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ScientificDegreeSerializer, TeachingCategorySerializer, ClassTypeSerializer, SemesterSerializer, TimePeriodSerializer, CarmenTableSerializer
from ...serializers_csv import CareerSerializerCSV, CarmenTableSerializerCSV, ClassTypeSerializerCSV, DepartmentSerializerCSV, FacultySerializerCSV, ProfessorSerializerCSV, ScientificDegreeSerializerCSV, SemesterSerializerCSV, StudyPlanSerializerCSV, SubjectSerializerCSV, TeachingCategorySerializerCSV, TeachingGroupSerializerCSV, TimePeriodSerializerCSV


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('-m', '--model', type=str)

    def handle(self, *args, **options):
        model_name = options['model'] if options['model'] else 'All'

        if model_name == 'All':
            self.fill_all()
        else:
            self.get_model_data(model_name)

    def fill_all(self):
        print('All')
        pass

    def get_model_data(self, model_name: str):
        data: list[dict] = []
        file_dir = self.get_file_dir(model_name)

        if file_dir == 'error':
            print('Error, not valid model_name, try again')
            return

        fieldnames = []
        with open(file_dir, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for count, row in enumerate(csv_reader):
                if count == 0:
                    fieldnames = row
                else:
                    field: dict = {}
                    for i, fieldname in enumerate(fieldnames):
                        field[fieldname] = row[i]
                    data.append(field)

        print(data)
        return data

    def get_file_dir(self, model_name: str):
        CURRENT_PATH = os.path.dirname(__file__)
        SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')
        PROFESSOR_DIR = os.path.join(
            CURRENT_PATH, '../../excels/professors.csv')
        FACULTY_DIR = os.path.join(CURRENT_PATH, '../../excels/faculties.csv')
        CAREER_DIR = os.path.join(CURRENT_PATH, '../../excels/careers.csv')
        STUDY_PLAN_DIR = os.path.join(
            CURRENT_PATH, '../../excels/study_plans.csv')
        DEPARTMENT_DIR = os.path.join(
            CURRENT_PATH, '../../excels/departments.csv')
        SEMESTER_DIR = os.path.join(CURRENT_PATH, '../../excels/semesters.csv')
        CLASS_TYPE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/class_types.csv')
        TIME_PERIOD_DIR = os.path.join(
            CURRENT_PATH, '../../excels/time_periods.csv')
        CARMEN_TABLE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/carmen_table.csv')
        TEACHING_GROUP_DIR = os.path.join(
            CURRENT_PATH, '../../excels/teaching_groups.csv')
        TEACHING_CATEGORY_DIR = os.path.join(
            CURRENT_PATH, '../../excels/teaching_categories.csv')
        SCIENTIFIC_DEGREE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/scientific_degrees.csv')

        if model_name == 'Careers':
            file_dir = CAREER_DIR
        elif model_name == 'CarmenTable':
            file_dir = CARMEN_TABLE_DIR
        elif model_name == 'ClassTypes':
            file_dir = CLASS_TYPE_DIR
        elif model_name == 'Departments':
            file_dir = DEPARTMENT_DIR
        elif model_name == 'Faculties':
            file_dir = FACULTY_DIR
        elif model_name == 'Professors':
            file_dir = PROFESSOR_DIR
        elif model_name == 'ScientificDegrees':
            file_dir = SCIENTIFIC_DEGREE_DIR
        elif model_name == 'Semesters':
            file_dir = SEMESTER_DIR
        elif model_name == 'StudyPlans':
            file_dir = STUDY_PLAN_DIR
        elif model_name == 'Subjects':
            file_dir = SUBJECTS_DIR
        elif model_name == 'TeachingCategories':
            file_dir = TEACHING_CATEGORY_DIR
        elif model_name == 'TeachingGroups':
            file_dir = TEACHING_GROUP_DIR
        elif model_name == 'TimePeriods':
            file_dir = TIME_PERIOD_DIR
        else:
            file_dir = 'error'
        return file_dir
