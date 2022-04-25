from pkg_resources import require
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
    teaching_groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = StudyPlan
        fields = '__all__'


class TeachingGroupSerializer(ModelSerializer):
    study_plan_id = serializers.IntegerField(required=True, write_only=True)
    study_plan = serializers.SerializerMethodField()

    def get_study_plan(self, obj) -> dict:
        if obj.study_plan:
            return {
                "id": obj.study_plan.id,
                "name": obj.study_plan.name
            }
        return None

    class Meta:
        model = TeachingGroup
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    career_id = serializers.IntegerField(required=True, write_only=True)
    career = serializers.SerializerMethodField()

    def get_career(self, obj) -> dict:
        if obj.career:
            return {
                "id": obj.career.id,
                "name": obj.career.name
            }
        return None

    class Meta:
        model = Department
        fields = '__all__'


class ClassTypeSerializer(ModelSerializer):
    class Meta:
        model = ClassType
        fields = '__all__'


class TimePeriodSerializer(ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = '__all__'


class SemesterSerializer(ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class ScientificDegreeSerializer(ModelSerializer):
    class Meta:
        model = ScientificDegree
        fields = '__all__'


class TeachingCategorySerializer(ModelSerializer):
    class Meta:
        model = TeachingCategory
        fields = '__all__'


class ProfessorSerializer(ModelSerializer):
    department_id = serializers.IntegerField(required=True, write_only=True)
    department = serializers.SerializerMethodField()

    scientific_degree_id = serializers.IntegerField(
        required=True, write_only=True)
    scientific_degree = serializers.SerializerMethodField()

    teaching_category_id = serializers.IntegerField(
        required=True, write_only=True)
    teaching_category = serializers.SerializerMethodField()

    def get_department(self, obj) -> dict:
        if obj.department:
            return {
                "id": obj.department.id,
                "name": obj.department.name,
            }
        return None

    def get_scientific_degree(self, obj) -> dict:
        if obj.scientific_degree:
            return {
                "id": obj.scientific_degree.id,
                "name": obj.scientific_degree.name,
            }
        return None

    def get_teaching_category(self, obj) -> dict:
        if obj.teaching_category:
            return {
                "id": obj.teaching_category.id,
                "name": obj.teaching_category.name,
            }
        return None

    class Meta:
        model = Professor
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    department_id = serializers.IntegerField(required=True, write_only=True)
    department = serializers.SerializerMethodField()

    career_id = serializers.IntegerField(required=True, write_only=True)
    career = serializers.SerializerMethodField()

    study_plan_id = serializers.IntegerField(required=True, write_only=True)
    study_plan = serializers.SerializerMethodField()

    def get_study_plan(self, obj) -> dict:
        if obj.study_plan:
            return {
                "id": obj.study_plan.id,
                "name": obj.study_plan.name
            }
        return None

    def get_career(self, obj) -> dict:
        if obj.career:
            return {
                "id": obj.career.id,
                "name": obj.career.name
            }
        return None

    def get_department(self, obj) -> dict:
        if obj.department:
            return {
                "id": obj.department.id,
                "name": obj.department.name,
            }
        return None

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectDescriptionSerializer(ModelSerializer):
    subject_id = serializers.IntegerField(required=True, write_only=True)
    subject = serializers.SerializerMethodField()

    class_type_id = serializers.IntegerField(required=True, write_only=True)
    class_type = serializers.SerializerMethodField()

    time_period_id = serializers.IntegerField(required=True, write_only=True)
    time_period = serializers.SerializerMethodField()

    def get_subject(self, obj) -> dict:
        if obj.subject:
            return {
                "id": obj.subject.id,
                "name": obj.subject.name
            }
        return None

    def get_class_type(self, obj) -> dict:
        if obj.class_type:
            return {
                "id": obj.class_type.id,
                "name": obj.class_type.name
            }
        return None

    def get_time_period(self, obj) -> dict:
        if obj.time_period:
            return {
                "id": obj.time_period.id,
                "name": obj.time_period.name
            }
        return None

    class Meta:
        model = SubjectDescription
        fields = '__all__'


class TeachingAssignmentSerializer(ModelSerializer):
    professor = serializers.CharField(source='professor.name')
    subjectDescription = serializers.CharField(
        source='subjectDescription.subject')

    class Meta:
        model = TeachingAssignment
        fields = ['id', 'percent', 'group', 'subjectDescription',
                  'professor']


class CarmenTableSerializer(ModelSerializer):
    teachingGroup = serializers.CharField(source='teachingGroup.name')
    timePeriod = serializers.CharField(source='timePeriod.name')
    semester = serializers.CharField(source='semester.name')

    class Meta:
        model = CarmenTable
        fields = ['id', 'teachingGroup', 'timePeriod', 'semester']
