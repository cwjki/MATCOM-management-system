from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CarmenTable, Faculty, Career, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, ScientificDegree, TeachingCategory, Professor, Subject, Semester, TimePeriod


class CareerSerializerCSV(ModelSerializer):
    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.faculty:
            return obj.faculty.name
        return None

    class Meta:
        model = Career
        exclude = ['id']


class StudyPlanSerializerCSV(ModelSerializer):
    class Meta:
        model = StudyPlan
        exclude = ['id']


class TeachingGroupSerializerCSV(ModelSerializer):
    class Meta:
        model = TeachingGroup
        exclude = ['id']


class FacultySerializerCSV(ModelSerializer):

    class Meta:
        model = Faculty
        exclude = ['id']


class DepartmentSerializerCSV(ModelSerializer):
    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.faculty:
            return obj.faculty.name
        return None

    class Meta:
        model = Department
        exclude = ['id']


class ClassTypeSerializerCSV(ModelSerializer):
    class Meta:
        model = ClassType
        exclude = ['id']


class TimePeriodSerializerCSV(ModelSerializer):
    class Meta:
        model = TimePeriod
        exclude = ['id']


class SemesterSerializerCSV(ModelSerializer):
    class Meta:
        model = Semester
        exclude = ['id']


class ScientificDegreeSerializerCSV(ModelSerializer):
    class Meta:
        model = ScientificDegree
        exclude = ['id']


class TeachingCategorySerializerCSV(ModelSerializer):
    class Meta:
        model = TeachingCategory
        exclude = ['id']


class ProfessorSerializerCSV(ModelSerializer):
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    scientific_degree = serializers.SerializerMethodField()
    teaching_category = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.department:
            return obj.department.faculty.name
        return None

    def get_department(self, obj) -> dict:
        if obj.department:
            return obj.department.name
        return None

    def get_scientific_degree(self, obj) -> dict:
        if obj.scientific_degree:
            return obj.scientific_degree.name
        return None

    def get_teaching_category(self, obj) -> dict:
        if obj.teaching_category:
            return obj.teaching_category.name
        return None

    class Meta:
        model = Professor
        exclude = ['id']


class SubjectSerializerCSV(ModelSerializer):
    department = serializers.SerializerMethodField()
    career = serializers.SerializerMethodField()
    study_plan = serializers.SerializerMethodField()
    semester = serializers.SerializerMethodField()

    def get_semester(self, obj) -> dict:
        if obj.semester:
            return obj.semester.name
        return None

    def get_study_plan(self, obj) -> dict:
        if obj.study_plan:
            return obj.study_plan.name
        return None

    def get_career(self, obj) -> dict:
        if obj.career:
            return obj.career.name
        return None

    def get_department(self, obj) -> dict:
        if obj.department:
            return obj.department.name
        return None

    class Meta:
        model = Subject
        exclude = ['id']


class CarmenTableSerializerCSV(ModelSerializer):
    teaching_group = serializers.SerializerMethodField()
    time_period = serializers.SerializerMethodField()
    semester = serializers.SerializerMethodField()
    study_plan = serializers.SerializerMethodField()

    def get_teaching_group(self, obj) -> dict:
        if obj.teaching_group:
            return obj.teaching_group.name
        return None

    def get_time_period(self, obj) -> dict:
        if obj.time_period:
            return obj.time_period.name
        return None

    def get_semester(self, obj) -> dict:
        if obj.semester:
            return obj.semester.name
        return None

    def get_study_plan(self, obj) -> dict:
        if obj.study_plan:
            return obj.study_plan.name
        return None

    class Meta:
        model = CarmenTable
        exclude = ['id']


class SubjectDescriptionSerializerCSV(ModelSerializer):
    subject = serializers.SerializerMethodField()
    study_plan = serializers.SerializerMethodField()
    career = serializers.SerializerMethodField()
    class_type = serializers.SerializerMethodField()
    time_period = serializers.SerializerMethodField()
    teaching_group = serializers.SerializerMethodField()

    def get_subject(self, obj) -> dict:
        if obj.subject:
            return obj.subject.name
        return None

    def get_study_plan(self, obj) -> dict:
        if obj.subject:
            return obj.subject.study_plan.name
        return None

    def get_career(self, obj) -> dict:
        if obj.subject:
            return obj.subject.career.name
        return None

    def get_class_type(self, obj) -> dict:
        if obj.class_type:
            return obj.class_type.name
        return None

    def get_time_period(self, obj) -> dict:
        if obj.time_period:
            return obj.time_period.name
        return None

    def get_teaching_group(self, obj) -> dict:
        if obj.teaching_group:
            return obj.teaching_group.name
        return None

    class Meta:
        model = SubjectDescription
        exclude = ['id']


class TeachingAssignmentSerializerCSV(ModelSerializer):
    professor_name = serializers.SerializerMethodField()
    professor_last_name = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    career = serializers.SerializerMethodField()
    teaching_group = serializers.SerializerMethodField()
    study_plan = serializers.SerializerMethodField()
    class_type = serializers.SerializerMethodField()
    time_period = serializers.SerializerMethodField()

    def get_professor_name(self, obj) -> dict:
        if obj.professor:
            return obj.professor.name
        return None

    def get_professor_last_name(self, obj) -> dict:
        if obj.professor:
            return obj.professor.last_name
        return None

    def get_subject(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.subject.name
        return None

    def get_study_plan(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.subject.study_plan.name
        return None

    def get_career(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.subject.career.name
        return None

    def get_teaching_group(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.teaching_group.name
        return None

    def get_class_type(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.class_type.name
        return None

    def get_time_period(self, obj) -> dict:
        if obj.subject_description:
            return obj.subject_description.time_period.name
        return None

    class Meta:
        model = TeachingAssignment
        exclude = ['id', 'professor', 'subject_description']
