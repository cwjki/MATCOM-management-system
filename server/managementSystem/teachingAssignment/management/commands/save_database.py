import csv
import os
from django.core.management.base import BaseCommand, CommandError, CommandParser
from ...models import Professor, Subject, Faculty, Career, StudyPlan, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester
from ...serializers import ProfessorSerializer, SubjectSerializer, FacultySerializer, CareerSerializer, StudyPlanSerializer, TeachingGroupSerializer, DepartmentSerializer, ScientificDegreeSerializer, TeachingCategorySerializer, ClassTypeSerializer, SemesterSerializer

CURRENT_PATH = os.path.dirname(__file__)
SUBJECTS_DIR = os.path.join(CURRENT_PATH, '../../excels/subjects.csv')
PROFESSOR_DIR = os.path.join(CURRENT_PATH, '../../excels/professors.csv')
FACULTY_DIR = os.path.join(CURRENT_PATH, '../../excels/faculties.csv')
CAREER_DIR = os.path.join(CURRENT_PATH, '../../excels/careers.csv')
STUDY_PLAN_DIR = os.path.join(CURRENT_PATH, '../../excels/study_plans.csv')
DEPARTMENT_DIR = os.path.join(CURRENT_PATH, '../../excels/departments.csv')
SEMESTER_DIR = os.path.join(CURRENT_PATH, '../../excels/semesters.csv')
CLASS_TYPE_DIR = os.path.join(CURRENT_PATH, '../../excels/class_types.csv')
TEACHING_GROUP_DIR = os.path.join(
    CURRENT_PATH, '../../excels/teaching_groups.csv')
TEACHING_CATEGORY_DIR = os.path.join(
    CURRENT_PATH, '../../excels/teaching_categories.csv')
SCIENTIFIC_DEGREE_DIR = os.path.join(
    CURRENT_PATH, '../../excels/scientific_degrees.csv')


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        model_name = options['model_name']
        fieldnames, data, file_path = self.get_fieldnames_and_data(model_name)

        with open(file_path, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def get_fieldnames_and_data(self, name: str):
        if name == 'Subjects':
            queryset = Subject.objects.all()
            fieldnames = ['id', 'name', 'department', 'career',
                          'study_plan', 'semester', 'number_of_hours']
            data = [SubjectSerializer(subject).data for subject in queryset]
            file_path = SUBJECTS_DIR

        elif name == 'Professors':
            queryset = Professor.objects.all()
            fieldnames = ['id', 'name', 'last_name', 'department', 'scientific_degree',
                          'teaching_category', 'faculty']
            data = [ProfessorSerializer(
                professor).data for professor in queryset]
            file_path = PROFESSOR_DIR

        elif name == 'Faculties':
            queryset = Faculty.objects.all()
            fieldnames = ['id', 'name', ]
            data = [FacultySerializer(faculty).data for faculty in queryset]
            file_path = FACULTY_DIR

        elif name == 'Careers':
            queryset = Career.objects.all()
            fieldnames = ['id', 'name', 'faculty']
            data = [CareerSerializer(career).data for career in queryset]
            file_path = CAREER_DIR

        elif name == 'StudyPlans':
            queryset = StudyPlan.objects.all()
            fieldnames = ['id', 'name',
                          'number_of_semesters', 'until', 'since']
            data = [StudyPlanSerializer(
                study_plan).data for study_plan in queryset]
            file_path = STUDY_PLAN_DIR

        elif name == 'TeachingGroups':
            queryset = TeachingGroup.objects.all()
            fieldnames = ['id', 'name']
            data = [TeachingGroupSerializer(
                teaching_group).data for teaching_group in queryset]
            file_path = TEACHING_GROUP_DIR

        elif name == 'Departments':
            queryset = Department.objects.all()
            fieldnames = ['id', 'name', 'faculty']
            data = [DepartmentSerializer(
                dapartment).data for dapartment in queryset]
            file_path = DEPARTMENT_DIR

        elif name == 'ScientificDegrees':
            queryset = ScientificDegree.objects.all()
            fieldnames = ['id', 'name']
            data = [ScientificDegreeSerializer(
                scientific_degree).data for scientific_degree in queryset]
            file_path = SCIENTIFIC_DEGREE_DIR

        elif name == 'TeachingCategories':
            queryset = TeachingCategory.objects.all()
            fieldnames = ['id', 'name']
            data = [TeachingCategorySerializer(
                teaching_category).data for teaching_category in queryset]
            file_path = TEACHING_CATEGORY_DIR
        
        elif name == 'Semesters':
            queryset = Semester.objects.all()
            fieldnames = ['id', 'name']
            data = [SemesterSerializer(
                semester).data for semester in queryset]
            file_path = SEMESTER_DIR
        
        elif name == 'ClassTypes':
            queryset = ClassType.objects.all()
            fieldnames = ['id', 'name']
            data = [ClassTypeSerializer(
                class_type).data for class_type in queryset]
            file_path = CLASS_TYPE_DIR

        else:
            print("error")

        return fieldnames, data, file_path
