import random
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

        # Create a list of cost of each assignment
        rows, cols = (15, 22)
        cost = [[0] * cols] * rows
        for i in range(0, rows):
            for j in range(0, cols):
                r = random.randrange(10)
                cost[i][j] = r

        # The cost data is made into a dictionary
        cost = makeDict([subjects, professors], cost)

        # Creates the problem variable to contain the problem data
        problem = LpProblem("Teaching_Assignment_Problem", LpMaximize)

        # Creates a list of tuples containing all the possible teaching assignments
        teachingAssignments = [(subject, professor)
                               for subject in subjects for professor in professors]

        # Set teachingAssignments to take either 1 or 0 values (professor taking the class)
        ta = LpVariable.dicts("TeachingAssignments",
                              (subjects, professors), 0, None, LpInteger)

        # Define Objective Function
        problem += (
            lpSum(ta[s][p] * cost[s][p] for (s, p) in teachingAssignments)
        )
