from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Snippet, Career, StudyPlan, SchoolYear, Department


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
