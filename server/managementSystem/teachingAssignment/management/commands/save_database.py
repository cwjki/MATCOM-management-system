import csv
import os
from django.core.management.base import BaseCommand, CommandParser

from ...models import Professor, Subject, Faculty, Career, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester, TimePeriod, CarmenTable
from ...serializers_csv import CareerSerializerCSV, CarmenTableSerializerCSV, ClassTypeSerializerCSV, DepartmentSerializerCSV, FacultySerializerCSV, ProfessorSerializerCSV, ScientificDegreeSerializerCSV, SemesterSerializerCSV, StudyPlanSerializerCSV, SubjectDescriptionSerializerCSV, SubjectSerializerCSV, TeachingAssignmentSerializerCSV, TeachingCategorySerializerCSV, TeachingGroupSerializerCSV, TimePeriodSerializerCSV
from thesisAssignment.models import Place, Keyword, Thesis, ThesisCommittee
from thesisAssignment.serializers_csv import PlaceSerializerCSV, KeywordSerializerCSV, ThesisCommitteeSerializerCSV, ThesisSerializerCSV


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('-m', '--model', type=str)

    def handle(self, *args, **options):
        model_name = options['model'] if options['model'] else 'All'

        if model_name == 'All':
            self.save_all()
        else:
            self.save_model(model_name)

    def save_all(self):
        models_names = ['ClassTypes', 'Faculties',
                        'ScientificDegrees', 'TeachingCategories',
                        'Semesters', 'TeachingGroups', 'TimePeriods',
                        'Careers', 'StudyPlans', 'CarmenTable', 'Departments',
                        'Subjects', 'Professors', 'SubjectDescriptions', 'TeachingAssignments',
                        'Places', 'Keywords', 'Thesis', 'ThesisCommittee']

        for model_name in models_names:
            self.save_model(model_name)

    def save_model(self, model_name: str):
        file_dir = self.get_file_dir(model_name)

        if file_dir == 'error':
            print(f'Error, not valid model_name: {model_name}, try again')
            return

        fieldnames, data = self.get_fieldnames_and_data(model_name)

        with open(file_dir, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def get_fieldnames_and_data(self, model_name: str):
        if model_name == 'Subjects':
            queryset = Subject.objects.all()
            fieldnames = ['name', 'department', 'career',
                          'study_plan', 'semester', 'number_of_hours']
            data = [SubjectSerializerCSV(subject).data for subject in queryset]

        elif model_name == 'Professors':
            queryset = Professor.objects.all()
            fieldnames = ['name', 'last_name', 'department', 'scientific_degree',
                          'teaching_category', 'faculty']
            data = [ProfessorSerializerCSV(
                professor).data for professor in queryset]

        elif model_name == 'Faculties':
            queryset = Faculty.objects.all()
            fieldnames = ['name', ]
            data = [FacultySerializerCSV(faculty).data for faculty in queryset]

        elif model_name == 'Careers':
            queryset = Career.objects.all()
            fieldnames = ['name', 'faculty']
            data = [CareerSerializerCSV(career).data for career in queryset]

        elif model_name == 'StudyPlans':
            queryset = StudyPlan.objects.all()
            fieldnames = ['name',
                          'number_of_semesters', 'until', 'since']
            data = [StudyPlanSerializerCSV(
                study_plan).data for study_plan in queryset]

        elif model_name == 'TeachingGroups':
            queryset = TeachingGroup.objects.all()
            fieldnames = ['name']
            data = [TeachingGroupSerializerCSV(
                teaching_group).data for teaching_group in queryset]

        elif model_name == 'Departments':
            queryset = Department.objects.all()
            fieldnames = ['name', 'faculty']
            data = [DepartmentSerializerCSV(
                dapartment).data for dapartment in queryset]

        elif model_name == 'ScientificDegrees':
            queryset = ScientificDegree.objects.all()
            fieldnames = ['name']
            data = [ScientificDegreeSerializerCSV(
                scientific_degree).data for scientific_degree in queryset]

        elif model_name == 'TeachingCategories':
            queryset = TeachingCategory.objects.all()
            fieldnames = ['name']
            data = [TeachingCategorySerializerCSV(
                teaching_category).data for teaching_category in queryset]

        elif model_name == 'Semesters':
            queryset = Semester.objects.all()
            fieldnames = ['name']
            data = [SemesterSerializerCSV(
                semester).data for semester in queryset]

        elif model_name == 'ClassTypes':
            queryset = ClassType.objects.all()
            fieldnames = ['name']
            data = [ClassTypeSerializerCSV(
                class_type).data for class_type in queryset]

        elif model_name == 'TimePeriods':
            queryset = TimePeriod.objects.all()
            fieldnames = ['name']
            data = [TimePeriodSerializerCSV(
                time_period).data for time_period in queryset]

        elif model_name == 'CarmenTable':
            queryset = CarmenTable.objects.all()
            fieldnames = ['teaching_group',
                          'study_plan', 'semester', 'time_period']
            data = [CarmenTableSerializerCSV(
                carmen_table).data for carmen_table in queryset]

        elif model_name == 'SubjectDescriptions':
            queryset = SubjectDescription.objects.all()
            fieldnames = ['subject', 'career', 'study_plan', 'class_type', 'time_period',
                          'number_of_groups', 'scholar_year', 'number_of_hours']
            data = [SubjectDescriptionSerializerCSV(
                subject_description).data for subject_description in queryset]

        elif model_name == 'TeachingAssignments':
            queryset = TeachingAssignment.objects.all()
            fieldnames = ['professor_name', 'professor_last_name', 'career', 'study_plan',
                          'subject', 'class_type', 'time_period', 'scholar_year', 'percent', 'group']
            data = [TeachingAssignmentSerializerCSV(
                teaching_assignment).data for teaching_assignment in queryset]

        elif model_name == 'Places':
            queryset = Place.objects.all()
            fieldnames = ['name']
            data = [PlaceSerializerCSV(
                place).data for place in queryset]

        elif model_name == 'Keywords':
            queryset = Keyword.objects.all()
            fieldnames = ['name']
            data = [KeywordSerializerCSV(
                keyword).data for keyword in queryset]

        elif model_name == 'Thesis':
            queryset = Thesis.objects.all()
            fieldnames = ['title', 'student',
                          'tutor', 'cotutors', 'keywords']
            data = [ThesisSerializerCSV(
                thesis).data for thesis in queryset]

        elif model_name == 'ThesisCommittee':
            queryset = ThesisCommittee.objects.all()
            fieldnames = ['date', 'time', 'thesis', 'place',
                          'opponent', 'secretary', 'president']
            data = [ThesisCommitteeSerializerCSV(
                thesis_committee).data for thesis_committee in queryset]

        return fieldnames, data

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
        SUBJECT_DESCRIPTION_DIR = os.path.join(
            CURRENT_PATH, '../../excels/subject_descriptions.csv')
        TEACHING_ASSIGNMENT_DIR = os.path.join(
            CURRENT_PATH, '../../excels/teaching_assignments.csv')
        PLACE_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/places.csv')
        KEYWORD_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/keywords.csv')
        THESIS_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/thesis.csv')
        THESIS_COMMITTEE_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/thesis_committee.csv')

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
        elif model_name == 'SubjectDescriptions':
            file_dir = SUBJECT_DESCRIPTION_DIR
        elif model_name == 'TeachingAssignments':
            file_dir = TEACHING_ASSIGNMENT_DIR
        elif model_name == 'Places':
            file_dir = PLACE_DIR
        elif model_name == 'Keywords':
            file_dir = KEYWORD_DIR
        elif model_name == 'Thesis':
            file_dir = THESIS_DIR
        elif model_name == 'ThesisCommittee':
            file_dir = THESIS_COMMITTEE_DIR
        else:
            file_dir = 'error'
        return file_dir
