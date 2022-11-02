from asyncore import read, write
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CarmenTable, Faculty, Career, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, ScientificDegree, TeachingCategory, Professor, Subject, Semester, TeachingPlanning, TimePeriod


class FacultySerializer(ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'


class CareerSerializer(ModelSerializer):
    faculty_id = serializers.IntegerField(required=True, write_only=True)
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = Career
        fields = '__all__'


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'


class TeachingGroupSerializer(ModelSerializer):

    class Meta:
        model = TeachingGroup
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    faculty_id = serializers.IntegerField(required=True, write_only=True)
    faculty = FacultySerializer(read_only=True)

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
    department = DepartmentSerializer(read_only=True)

    scientific_degree_id = serializers.IntegerField(
        required=True, write_only=True)
    scientific_degree = ScientificDegreeSerializer(read_only=True)

    teaching_category_id = serializers.IntegerField(
        required=True, write_only=True)
    teaching_category = TeachingCategorySerializer(read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    department_id = serializers.IntegerField(required=True, write_only=True)
    department = DepartmentSerializer(read_only=True)

    career_id = serializers.IntegerField(required=True, write_only=True)
    career = CareerSerializer(read_only=True)

    study_plan_id = serializers.IntegerField(required=True, write_only=True)
    study_plan = StudyPlanSerializer(read_only=True)

    semester_id = serializers.IntegerField(required=True, write_only=True)
    semester = SemesterSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectDescriptionSerializer(ModelSerializer):
    subject_id = serializers.IntegerField(write_only=True)
    subject = SubjectSerializer(read_only=True)

    class_type_id = serializers.IntegerField(required=True, write_only=True)
    class_type = ClassTypeSerializer(read_only=True)

    time_period_id = serializers.IntegerField(required=True, write_only=True)
    time_period = TimePeriodSerializer(read_only=True)

    teaching_group_id = serializers.IntegerField(
        required=True, write_only=True)
    teaching_group = TeachingGroupSerializer(read_only=True)

    def create(self, validated_data):
        subject_description = SubjectDescription.objects.create(
            **validated_data)

        number_of_groups = validated_data['number_of_groups']
        for _ in range(0, number_of_groups):
            TeachingAssignment.objects.create(
                subject_description_id=subject_description.id)

        return subject_description

    class Meta:
        model = SubjectDescription
        fields = '__all__'


class TeachingAssignmentSerializer(ModelSerializer):
    professor_id = serializers.IntegerField(required=True, write_only=True)
    professor = ProfessorSerializer(read_only=True)

    subject_description_id = serializers.IntegerField(
        required=True, write_only=True)
    subject_description = SubjectDescriptionSerializer(read_only=True)

    class Meta:
        model = TeachingAssignment
        fields = '__all__'


class CarmenTableSerializer(ModelSerializer):
    teaching_group_id = serializers.IntegerField(
        required=True, write_only=True)
    teaching_group = TeachingGroupSerializer(read_only=True)

    time_period_id = serializers.IntegerField(
        required=True, write_only=True)
    time_period = TimePeriodSerializer(read_only=True)

    semester_id = serializers.IntegerField(
        required=True, write_only=True)
    semester = SemesterSerializer(read_only=True)

    study_plan_id = serializers.IntegerField(
        required=True, write_only=True)
    study_plan = StudyPlanSerializer(read_only=True)

    class Meta:
        model = CarmenTable
        fields = '__all__'


class TeachingPlanningSerializer(ModelSerializer):
    teaching_assignments = TeachingAssignmentSerializer(
        read_only=True, many=True)

    class Meta:
        model = TeachingPlanning
        fields = '__all__'
