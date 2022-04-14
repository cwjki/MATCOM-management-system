from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Snippet, Career, StudyPlan, TeachingGroup, Department, ClassType, ScientificDegree, TeachingCategory, Professor, Subject, SubjectDescription, TeachingAssignment, Semester, CarmenTable, TimePeriod


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
    teachingGroups = serializers.StringRelatedField(many=True)

    class Meta:
        model = StudyPlan
        fields = ['id', 'name', 'since', 'until',
                  'numberOfSemesters', 'teachingGroups']


class TeachingGroupSerializer(ModelSerializer):
    studyPlan = serializers.CharField(source='studyPlan.name')

    class Meta:
        model = TeachingGroup
        fields = ['id', 'name', 'studyPlan']


class DepartmentSerializer(ModelSerializer):
    career = serializers.CharField(source='career.name')

    class Meta:
        model = Department
        fields = ['id', 'name', 'career']


class ClassTypeSerializer(ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id', 'name']


class TimePeriodSerializer(ModelSerializer):
    class Meta:
        model = TimePeriod
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
    department = serializers.CharField(source='department.name')
    scientificDegree = serializers.CharField(source='scientificDegree.name')
    teachingCategory = serializers.CharField(source='teachingCategory.name')

    class Meta:
        model = Professor
        fields = ['id', 'name', 'lastName', 'department',
                  'scientificDegree', 'teachingCategory']


class SubjectSerializer(ModelSerializer):
    department = serializers.CharField(source='department.name')
    career = serializers.CharField(source='career.name')
    studyPlan = serializers.CharField(source='studyPlan.name')

    class Meta:
        model = Subject
        fields = ['id', 'name', 'numberOfHours', 'semester',
                  'career', 'department', 'studyPlan']


class SubjectDescriptionSerializer(ModelSerializer):
    subject = serializers.CharField(source='subject.name')
    classType = serializers.CharField(source='classType.name')
    timePeriod = serializers.CharField(source='timePeriod.name')

    class Meta:
        model = SubjectDescription
        fields = ['id', 'numberOfHours', 'numberOfGroups', 'subject',
                  'classType', 'timePeriod']


class TeachingAssignmentSerializer(ModelSerializer):
    class Meta:
        model = TeachingAssignment
        fields = ['id', 'percent', 'group', 'subjectDescription',
                  'professor']


class CarmenTableSerializer(ModelSerializer):
    class Meta:
        model = CarmenTable
        fields = ['id', 'teachingGroup', 'timePeriod', 'semester']
