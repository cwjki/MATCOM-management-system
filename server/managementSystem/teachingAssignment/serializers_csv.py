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
