from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Snippet, Career, StudyPlan, SchoolYear, Department, ClassType, ScientificDegree, TeachingCategory, YearPeriod, Professor, Subject, TeachingPlanning, TeachingAssignment, Semester, CarmenTable


class SnippetSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'owner']


class UserSerializer(ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    careers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Career.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'careers']


class CareerSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Career
        fields = ['id', 'name', 'owner']


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['id', 'name', 'since', 'until', 'numberOfSemesters']


class SchoolYearSerializer(ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name', 'studyPlan']


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'career']


class ClassTypeSerializer(ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id', 'name']


class YearPeriodSerializer(ModelSerializer):
    class Meta:
        model = YearPeriod
        fields = ['id', 'name']


class SemesterSerializer(ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'name']


class ScientificDegreeSerializer(ModelSerializer):
    class Meta:
        model = ScientificDegree
        fields = ['id', 'name']


class TeachingCategorySerializer(ModelSerializer):
    class Meta:
        model = TeachingCategory
        fields = ['id', 'name']


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'name', 'lastName', 'department',
                  'scientificDegree', 'teachingCategory']


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'numberOfHours', 'semester',
                  'career', 'department', 'studyPlan']


class TeachingPlanningSerializer(ModelSerializer):
    class Meta:
        model = TeachingPlanning
        fields = ['id', 'numberOfHours', 'numberOfGroups', 'subject',
                  'classType', 'yearPeriod']


class TeachingAssignmentSerializer(ModelSerializer):
    class Meta:
        model = TeachingAssignment
        fields = ['id', 'percent', 'group', 'teachingPlanning',
                  'professor']

class CarmenTableSerializer(ModelSerializer):
    class Meta:
        model = CarmenTable
        fields = ['id', 'schoolYear', 'yearPeriod', 'semester']
