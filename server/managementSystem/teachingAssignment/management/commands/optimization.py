import random
from unittest import result
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
        costs = makeDict([subjects, professors], cost)

        # Creates the problem variable to contain the problem data
        problem = LpProblem("Teaching_Assignment_Problem", LpMaximize)

        # Creates a list of tuples containing all the possible teaching assignments
        teachingAssignments = [(subject, professor)
                               for subject in subjects for professor in professors]

        # Set teachingAssignments to take either 1 or 0 values (professor taking the class)
        ta = LpVariable.dicts("ta",
                              (subjects, professors), 0, 1, LpInteger)

        # Define Objective Function
        problem += (
            lpSum(ta[s][p] * costs[s][p] for (s, p) in teachingAssignments)
        )

        # Define the constrains

        # Number of professor per subject
        for s in subjects:
            problem += (
                lpSum([ta[s][p] for p in professors]) == subject_groups[s],
                f'Number_of_professors_for_subject {s}',
            )

        # Maximum number of hours a teacher can have
        for p in professors:
            problem += (
                lpSum([ta[s][p] for s in subjects]) <= 4,
                f'Maximum_number_of_hours_for_professor {p}',
            )

        # The problem is solved using PuLP's choice of Solver
        problem.solve()

        results = [v.name for v in problem.variables() if v.varValue == 1]
        print(results)

        # The optimised objective function value is printed to the screen
        print("Value of Objective Function = ", value(problem.objective))


    def get_result_ids(self, result: list) -> list:
        '''
        Return a list of tuples '(subject_id, professor_id)' from the result list
        '''
        ids = []
        for ta in result:
            ta = [int(s) for s in ta.split('_') if s.isdigit()]
            ids.append((ta[0], ta[1]))

        return ids
