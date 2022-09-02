from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CarmenTable, Faculty, Career, Student, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, ScientificDegree, TeachingCategory, Professor, Subject, Semester, TeachingPlanning, Thesis, ThesisCommittee, TimePeriod


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
