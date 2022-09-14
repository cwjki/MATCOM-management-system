import random
from pulp import *


class OptimizationModel():
    def __init__(self, qs_subject, qs_professor) -> None:
        self.subjects = []
        self.professors = []
        self.subject_groups = {}
        self.subject_hours = {}

        self.get_queryset_data(qs_subject, qs_professor)

    def get_queryset_data(self, qs_subject, qs_professor):
        # Get subject description data
        for subject in qs_subject:
            self.subjects.append(subject.id)
            self.subject_groups[subject.id] = subject.number_of_groups
            self.subject_hours[subject.id] = subject.number_of_hours
        # Get the professors ids
        self.professors = [professor.id for professor in qs_professor]

    def get_result_ids(self, results: list) -> list:
        '''
        Return a list of tuples '(subject_id, professor_id)' from the result list
        '''
        ids = {}
        for ta in results:
            ta = [int(s) for s in ta.split('_') if s.isdigit()]
            ids[ta[0]] = ta[1]
        return ids

    def compute_costs(self):
        # Create a list of cost of each assignment
        rows, cols = (15, 22)
        cost = [[0] * cols] * rows
        for i in range(0, rows):
            for j in range(0, cols):
                r = random.randrange(10)
                cost[i][j] = r

        # The cost data is made into a dictionary
        costs = makeDict([self.subjects, self.professors], cost)
        return costs

    def solve(self):
        # Creates the problem variable to contain the problem data
        problem = LpProblem("Teaching_Assignment_Problem", LpMaximize)

        # Creates a list of tuples containing all the possible teaching assignments
        teachingAssignments = [(subject, professor)
                               for subject in self.subjects for professor in self.professors]

        # Set teachingAssignments to take either 1 or 0 values (professor taking the class)
        ta = LpVariable.dicts("ta",
                              (self.subjects, self.professors), 0, 1, LpInteger)

        costs = self.compute_costs()

        # Define Objective Function
        problem += (
            lpSum(ta[s][p] * costs[s][p] for (s, p) in teachingAssignments)
        )

        # Define the constrains

        # Number of professor per subject
        for s in self.subjects:
            problem += (
                lpSum([ta[s][p] for p in self.professors]
                      ) == self.subject_groups[s],
                f'Number_of_professors_for_subject {s}',
            )

        # Maximum number of hours a teacher can have
        for p in self.professors:
            problem += (
                lpSum([ta[s][p] for s in self.subjects]) <= 4,
                f'Maximum_number_of_hours_for_professor {p}',
            )

        # The problem is solved using PuLP's choice of Solver
        problem.solve()

        results = [v.name for v in problem.variables() if v.varValue == 1]
        results = self.get_result_ids(results)
        results['score'] = value(problem.objective)
        return results
