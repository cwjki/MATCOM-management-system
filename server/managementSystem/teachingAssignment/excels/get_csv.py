import csv
from typing import List
from ..models import TeachingAssignment
from ..serializers import TeachingAssignmentSerializer


class TeachingAssignmentInfo:
    def __init__(self) -> None:
        self.subject_name = ''
        self.scholar_year = ''
        self.conf_professors = ''
        self.conf_groups = 0
        self.conf_hours = 0
        self.cp_professors = ''
        self.cp_groups = 0
        self.cp_hours = 0
        self.faculty = 'MATCOM'
        self.course_type = 'CRD'
        self.number_of_hours = 0

    def __repr__(self) -> str:
        return (
            f'Asignatura: {self.subject_name} \n'
            f'Año: {self.scholar_year} \n'
            f'Grupos: {self.conf_groups}/{self.cp_groups} \n'
            f'Horas: {self.number_of_hours} \n'
            f'Profesores de C: {self.conf_professors} \n'
            f'Profesores de CP: {self.cp_professors} \n \n')


class TeachingAssignmentInfoCollection:
    def __init__(self) -> None:
        self.teaching_assignments: List[TeachingAssignmentInfo] = []

    def proccess_info(self, teaching_assignments: List[dict]):
        '''Main function to analize all teaching assignments'''
        for teaching_assignment in teaching_assignments:
            self.analize_row(teaching_assignment)
        self.compute_total_hours()

    def compute_total_hours(self):
        '''Compute the total hours of a subject'''
        for ta in self.teaching_assignments:
            conf_hours = ta.conf_hours / ta.conf_groups if ta.conf_groups != 0 else 0
            cp_hours = ta.cp_hours / ta.cp_groups if ta.cp_groups != 0 else 0
            ta.number_of_hours = conf_hours + cp_hours

    def analize_row(self, teaching_assignment: dict):
        '''Compute and save all the important data of a teaching assignment'''
        # get data
        subject_name = teaching_assignment['subject_description']['name']
        scholar_year = teaching_assignment['subject_description']['scholar_year']
        class_type = teaching_assignment['subject_description']['class_type']
        number_of_hours = teaching_assignment['subject_description']['number_of_hours']
        total_hours = teaching_assignment['subject_description']['total_hours']
        percent = teaching_assignment['percent']
        group = teaching_assignment['group']
        number_of_groups = teaching_assignment['subject_description']['number_of_groups']
        professor_hours = float(percent / 100) * number_of_hours
        professor_name = teaching_assignment['professor']['name'] + ' ' \
            + teaching_assignment['professor']['last_name']

        # check if the teaching assignments already exists
        already_exists, ta = self.contains(teaching_assignment)
        if not already_exists:
            ta = TeachingAssignmentInfo()
            self.teaching_assignments.append(ta)

        # add the data to the teaching asignment
        if class_type == 'Conferencia':
            ta.conf_groups = number_of_groups
            ta.conf_hours += professor_hours
            ta.conf_professors += f'C: {professor_name} ({professor_hours}) ({group}) \n'
        elif class_type == 'Clase Práctica':
            ta.cp_groups = number_of_groups
            ta.cp_hours += professor_hours
            ta.cp_professors += f'CP: {professor_name} ({professor_hours}) ({group}) \n'
        else:
            pass

        ta.subject_name = subject_name
        ta.scholar_year = scholar_year
        ta.number_of_hours = total_hours

    def contains(self, teaching_assignment: dict):
        '''
        Check if the teaching assignment already exists looking for the subject_name and scholar_year field.
        Returns a tuple <True or False>, <Instance or None>
        '''
        for ta in self.teaching_assignments:
            if ta.subject_name == teaching_assignment['subject_description']['name'] and ta.scholar_year == teaching_assignment['subject_description']['scholar_year']:
                return True, ta
        return False, None

    def print_info(self):
        for ta in self.teaching_assignments:
            print(ta)


class TA_CSV_GENERATOR():
    def __init__(self, department_name, file_dir) -> None:
        self.department = department_name
        self.csv_dir = file_dir

    def generate_csv(self):
        department_name = 'Matemática Aplicada'
        data = self.filter_by_department(department_name)

        fieldnames = ['Facultad', 'Tipo curso', 'Año',
                      'Asignatura', 'Horas', 'G', 'Profesor']

        ta_info = TeachingAssignmentInfoCollection()
        ta_info.proccess_info(data)

        rows = self.construct_fields(ta_info)
        fieldnames = ['Facultad', 'Tipo curso', 'Año',
                      'Asignatura', 'Horas', 'G', 'Profesor']

        with open(self.csv_dir, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def construct_fields(self, ta_info: TeachingAssignmentInfoCollection):
        result: List[dict] = []
        for ta in ta_info.teaching_assignments:
            row: dict = {}
            row['Facultad'] = ta.faculty
            row['Tipo curso'] = ta.course_type
            row['Año'] = ta.scholar_year
            row['Asignatura'] = ta.subject_name
            row['Horas'] = ta.number_of_hours
            row['G'] = f'{ta.conf_groups}/{ta.cp_groups}'
            row['Profesor'] = ta.conf_professors + ta.cp_professors
            result.append(row)
        return result

    def filter_by_department(self, department_name):
        queryset = TeachingAssignment.objects.all()
        data = [
            TeachingAssignmentSerializer(teachingAssignment).data
            for teachingAssignment in queryset]
        data = [
            teaching_assignment for teaching_assignment in data
            if teaching_assignment['subject_description']['department'] == department_name]

        excel_data = TeachingAssignmentInfoCollection()
        for teaching_assigment in data:
            excel_data.analize_row(teaching_assigment)

        return data
