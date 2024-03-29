import csv
import os

from django.core.management.base import BaseCommand, CommandParser

from ...models import Professor, Subject, Faculty, Career, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ScientificDegree, TeachingCategory, ClassType, Semester, TimePeriod, CarmenTable, ScholarYear
from thesisAssignment.models import Place, Keyword, Thesis, ThesisCommittee, ThesisDefense


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
        models_names = ['ClassTypes', 'Faculties',
                        'ScientificDegrees', 'TeachingCategories',
                        'Semesters', 'TeachingGroups', 'TimePeriods', 'ScholarYears',
                        'Careers', 'StudyPlans', 'CarmenTable', 'Departments',
                        'Subjects', 'Professors', 'SubjectDescriptions', 'TeachingAssignments',
                        'Places', 'Keywords', 'Thesis', 'ThesisCommittees', 'ThesisDefenses']

        for model_name in models_names:
            self.fill_model(model_name)

    def fill_model(self, model_name: str):
        data = self.get_model_data(model_name)

        if model_name == 'Careers':
            for obj in data:
                name = obj['name']
                faculty = Faculty.objects.get(name=obj['faculty'])
                career = Career(name=name, faculty=faculty)
                career.save()

        elif model_name == 'CarmenTable':
            for obj in data:
                semester = Semester.objects.get(name=obj['semester'])
                study_plan = StudyPlan.objects.get(name=obj['study_plan'])
                time_period = TimePeriod.objects.get(name=obj['time_period'])
                teaching_group = TeachingGroup.objects.get(
                    name=obj['teaching_group'])

                carmenTable = CarmenTable(
                    teaching_group=teaching_group,
                    study_plan=study_plan,
                    semester=semester,
                    time_period=time_period
                )
                carmenTable.save()

        elif model_name == 'ClassTypes':
            for obj in data:
                name = obj['name']
                class_type = ClassType(name=name)
                class_type.save()

        elif model_name == 'Departments':
            for obj in data:
                name = obj['name']
                faculty = Faculty.objects.get(name=obj['faculty'])
                department = Department(name=name, faculty=faculty)
                department.save()

        elif model_name == 'Faculties':
            for obj in data:
                name = obj['name']
                faculty = Faculty(name=name)
                faculty.save()

        elif model_name == 'Professors':
            for obj in data:
                name = obj['name']
                last_name = obj['last_name']
                # faculty = Faculty.objects.get(name=obj['faculty'])
                department = Department.objects.get(name=obj['department'])
                scientific_degree = ScientificDegree.objects.get(
                    name=obj['scientific_degree'])
                teaching_category = TeachingCategory.objects.get(
                    name=obj['teaching_category'])

                professor = Professor(
                    name=name,
                    last_name=last_name,
                    department=department,
                    scientific_degree=scientific_degree,
                    teaching_category=teaching_category
                )
                professor.save()

        elif model_name == 'ScientificDegrees':
            for obj in data:
                name = obj['name']
                scientific_degree = ScientificDegree(name=name)
                scientific_degree.save()

        elif model_name == 'Semesters':
            for obj in data:
                name = obj['name']
                semester = Semester(name=name)
                semester.save()

        elif model_name == 'StudyPlans':
            for obj in data:
                name = obj['name']
                number_of_semesters = obj['number_of_semesters']
                since = obj['since']
                until = obj['until'] if obj['until'] != '' else None

                study_plan = StudyPlan(
                    name=name,
                    number_of_semesters=number_of_semesters,
                    until=until,
                    since=since
                )
                study_plan.save()

        elif model_name == 'Subjects':
            for obj in data:
                name = obj['name']
                number_of_hours = obj['number_of_hours']
                department = Department.objects.get(name=obj['department'])
                career = Career.objects.get(name=obj['career'])
                study_plan = StudyPlan.objects.get(name=obj['study_plan'])
                semester = Semester.objects.get(name=obj['semester'])

                subject = Subject(
                    name=name,
                    department=department,
                    career=career,
                    study_plan=study_plan,
                    semester=semester,
                    number_of_hours=number_of_hours
                )
                subject.save()

        elif model_name == 'TeachingCategories':
            for obj in data:
                name = obj['name']
                teaching_category = TeachingCategory(name=name)
                teaching_category.save()

        elif model_name == 'TeachingGroups':
            for obj in data:
                name = obj['name']
                teaching_groups = TeachingGroup(name=name)
                teaching_groups.save()

        elif model_name == 'TimePeriods':
            for obj in data:
                name = obj['name']
                time_period = TimePeriod(name=name)
                time_period.save()

        elif model_name == 'ScholarYears':
            for obj in data:
                name = obj['name']
                current_year = obj['current_year']
                scholar_year = ScholarYear(
                    name=name, current_year=current_year)
                scholar_year.save()

        elif model_name == 'SubjectDescriptions':
            for obj in data:
                subject = obj['subject']
                number_of_hours = obj['number_of_hours']
                number_of_groups = obj['number_of_groups']
                career = Career.objects.get(name=obj['career'])
                class_type = ClassType.objects.get(name=obj['class_type'])
                time_period = TimePeriod.objects.get(name=obj['time_period'])
                scholar_year = ScholarYear.objects.get(
                    name=obj['scholar_year'])
                study_plan = StudyPlan.objects.get(name=obj['study_plan'])
                teaching_group = TeachingGroup.objects.get(
                    name=obj['teaching_group'])

                subject = Subject.objects.filter(
                    name=subject).filter(career=career).filter(study_plan=study_plan)[0]

                subject_description = SubjectDescription(
                    subject=subject,
                    class_type=class_type,
                    time_period=time_period,
                    scholar_year=scholar_year,
                    teaching_group=teaching_group,
                    number_of_hours=number_of_hours,
                    number_of_groups=number_of_groups
                )
                subject_description.save()

        elif model_name == 'TeachingAssignments':
            for obj in data:
                subject_name = obj['subject']
                professor_name = obj['professor_name']
                professor_last_name = obj['professor_last_name']
                percent = obj['percent']
                percent = percent if len(percent) else None
                group = obj['group']
                career = Career.objects.get(name=obj['career'])
                class_type = ClassType.objects.get(name=obj['class_type'])
                study_plan = StudyPlan.objects.get(name=obj['study_plan'])
                teaching_group = TeachingGroup.objects.get(
                    name=obj['teaching_group'])

                subject = Subject.objects.filter(name=subject_name).filter(
                    career=career).filter(study_plan=study_plan)[0]
                subject_description = SubjectDescription.objects.filter(subject=subject).filter(
                    teaching_group=teaching_group).filter(class_type=class_type)[0]
                professor = Professor.objects.filter(
                    last_name=professor_last_name).filter(name=professor_name)
                professor = professor[0] if len(professor) else None

                teaching_assignment = TeachingAssignment(
                    professor=professor,
                    subject_description=subject_description,
                    percent=percent,
                    group=group
                )
                teaching_assignment.save()

        elif model_name == 'Places':
            for obj in data:
                name = obj['name']
                place = Place(name=name)
                place.save()

        elif model_name == 'Keywords':
            for obj in data:
                name = obj['name']
                keyword = Keyword(name=name)
                keyword.save()

        elif model_name == 'Thesis':
            for obj in data:
                title = obj['title']
                student = obj['student']
                scholar_year: dict = eval(obj['scholar_year'])
                tutor: dict = eval(obj['tutor'])
                cotutors: list = eval(obj['cotutors'])
                keywords: list = eval(obj['keywords'])

                tutor = Professor.objects.filter(
                    last_name=tutor['last_name']).filter(name=tutor['name'])[0]

                scholar_year = ScholarYear.objects.get(
                    name=scholar_year['name'])

                thesis = Thesis(
                    title=title,
                    student=student,
                    tutor=tutor,
                    scholar_year=scholar_year
                )
                thesis.save()

                # Handle many to many field relations Cotutors and Keywords
                for ct in cotutors:
                    cotutor = Professor.objects.filter(
                        last_name=ct['last_name']).filter(name=ct['name'])[0]
                    thesis.cotutors.add(cotutor)

                for k in keywords:
                    keyword = Keyword.objects.filter(name=k['name'])[0]
                    thesis.keywords.add(keyword)

        elif model_name == 'ThesisCommittees':
            for obj in data:
                opponent: dict = eval(
                    obj['opponent']) if obj['opponent'] else None
                secretary: dict = eval(
                    obj['secretary']) if obj['secretary'] else None
                president: dict = eval(
                    obj['president']) if obj['president'] else None
                thesis: dict = eval(obj['thesis'])

                if opponent:
                    opponent = Professor.objects.filter(
                        last_name=opponent['last_name']).filter(name=opponent['name'])[0]
                if secretary:
                    secretary = Professor.objects.filter(
                        last_name=secretary['last_name']).filter(name=secretary['name'])[0]
                if president:
                    president = Professor.objects.filter(
                        last_name=president['last_name']).filter(name=president['name'])[0]
                thesis = Thesis.objects.filter(
                    student=thesis['student']).filter(title=thesis['title'])[0]

                thesis_committee = ThesisCommittee(
                    thesis=thesis,
                    opponent=opponent,
                    secretary=secretary,
                    president=president,
                )
                thesis_committee.save()

        elif model_name == 'ThesisDefenses':
            for obj in data:
                date = obj['date'] if obj['date'] else None
                time = obj['time'] if obj['time'] else None
                thesis_committee: dict = eval(obj['thesis_committee'])
                place: dict = eval(obj['place']) if obj['place'] else None

                if place:
                    place = Place.objects.filter(name=place['name'])[0]

                thesis = Thesis.objects.filter(
                    student=thesis_committee['student']).filter(title=thesis_committee['thesis_title'])[0]

                thesis_committee = ThesisCommittee.objects.filter(
                    thesis=thesis)[0]

                thesis_defense = ThesisDefense(
                    date=date,
                    time=time,
                    thesis_committee=thesis_committee,
                    place=place
                )
                thesis_defense.save()

    def get_model_data(self, model_name: str):
        data: list[dict] = []
        file_dir = self.get_file_dir(model_name)

        if file_dir == 'error':
            print(f'Error, not valid model_name: {model_name}, try again')
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
        return data

    def get_file_dir(self, model_name: str):
        CURRENT_PATH = os.path.dirname(__file__)
        SUBJECTS_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/subjects.csv')
        PROFESSOR_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/professors.csv')
        FACULTY_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/faculties.csv')
        CAREER_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/careers.csv')
        STUDY_PLAN_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/study_plans.csv')
        DEPARTMENT_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/departments.csv')
        SEMESTER_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/semesters.csv')
        CLASS_TYPE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/class_types.csv')
        TIME_PERIOD_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/time_periods.csv')
        SCHOLAR_YEAR_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/scholar_years.csv')
        CARMEN_TABLE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/carmen_table.csv')
        TEACHING_GROUP_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/teaching_groups.csv')
        TEACHING_CATEGORY_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/teaching_categories.csv')
        SCIENTIFIC_DEGREE_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/scientific_degrees.csv')
        SUBJECT_DESCRIPTION_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/subject_descriptions.csv')
        TEACHING_ASSIGNMENT_DIR = os.path.join(
            CURRENT_PATH, '../../excels/data/teaching_assignments.csv')
        PLACE_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/data/places.csv')
        KEYWORD_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/data/keywords.csv')
        THESIS_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/data/thesis.csv')
        THESIS_COMMITTEE_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/data/thesis_committees.csv')
        THESIS_DEFENSE_DIR = os.path.join(
            CURRENT_PATH, '../../../thesisAssignment/excels/data/thesis_defenses.csv')

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
        elif model_name == 'ScholarYears':
            file_dir = SCHOLAR_YEAR_DIR
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
        elif model_name == 'ThesisCommittees':
            file_dir = THESIS_COMMITTEE_DIR
        elif model_name == 'ThesisDefenses':
            file_dir = THESIS_DEFENSE_DIR

        else:
            file_dir = 'error'
        return file_dir
