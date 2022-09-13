from pulp import *
from django.core.management.base import BaseCommand, CommandParser

from ...models import Professor, SubjectDescription
from ...serializers import ProfessorSerializer, SubjectDescriptionSerializer


class Command(BaseCommand):
    help = 'Save database data in excels'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('-m', '--model', type=str)

    def handle(self, *args, **options):

        # Get subject description data
        queryset = SubjectDescription.objects.all()
        subjects = []
        subject_groups = {}
        subject_hours = {}
        for subject in queryset:
            subjects.append(subject.id)
            subject_groups[subject.id] = subject.number_of_groups
            subject_hours[subject.id] = subject.number_of_hours

        # Get the professors ids
        queryset = Professor.objects.all()
        professors = [professor.id for professor in queryset]

        # Creates the problem variable to contain the problem data
        problem = LpProblem("Teaching_Assignment_Problem", LpMaximize)

        # Creates a list of tuples containing all the possible teaching assignments
        teachingAssignments = [(subject, professor)
                               for subject in subjects for professor in professors]

        print(teachingAssignments)

        # teachingAssignments = LpVariable.dicts(
        #     "TeachingAssignments", professors, lowBound=0, upBound=1, cat='Integer')
