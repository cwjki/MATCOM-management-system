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
