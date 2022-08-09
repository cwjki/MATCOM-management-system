from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import CarmenTable, Faculty, Snippet, Career, Student, StudyPlan, SubjectDescription, TeachingAssignment, TeachingGroup, Department, ClassType, ScientificDegree, TeachingCategory, Professor, Subject, Semester, TeachingPlanning, Thesis, ThesisCommittee, TimePeriod


class SnippetSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'owner']


class UserSerializer(ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    # careers = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Career.objects.all())

    class Meta:
        model = User
        fields = '__all__'


class CareerSerializer(ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    faculty_id = serializers.IntegerField(required=True, write_only=True)
    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.faculty:
            return {
                "id": obj.faculty.id,
                "name": obj.faculty.name
            }
        return None

    class Meta:
        model = Career
        fields = '__all__'


class StudyPlanSerializer(ModelSerializer):
    # teaching_groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = StudyPlan
        fields = '__all__'


class TeachingGroupSerializer(ModelSerializer):
    # study_plan_id = serializers.IntegerField(required=True, write_only=True)
    # study_plan = serializers.SerializerMethodField()

    # def get_study_plan(self, obj) -> dict:
    #     if obj.study_plan:
    #         return {
    #             "id": obj.study_plan.id,
    #             "name": obj.study_plan.name
    #         }
    #     return None

    class Meta:
        model = TeachingGroup
        fields = '__all__'


class FacultySerializer(ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    faculty_id = serializers.IntegerField(required=True, write_only=True)
    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.faculty:
            return {
                "id": obj.faculty.id,
                "name": obj.faculty.name
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

    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj) -> dict:
        if obj.department:
            return {
                "id": obj.department.faculty.id,
                "name": obj.department.faculty.name,
            }
        return None

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

    semester_id = serializers.IntegerField(required=True, write_only=True)
    semester = serializers.SerializerMethodField()

    def get_semester(self, obj) -> dict:
        if obj.semester:
            return {
                "id": obj.semester.id,
                "name": obj.semester.name
            }
        return None

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

    scholar_year_id = serializers.IntegerField(required=True, write_only=True)
    scholar_year = serializers.SerializerMethodField()

    def get_subject(self, obj) -> dict:
        if obj.subject:
            return {
                "id": obj.subject.id,
                "name": obj.subject.name,
                "department": obj.subject.department.name,
                "career": obj.subject.career.name,
                "study_plan": obj.subject.study_plan.name,
                "semester": obj.subject.semester.name,
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

    def get_scholar_year(self, obj) -> dict:
        if obj.scholar_year:
            return {
                "id": obj.scholar_year.id,
                "teaching_group": obj.scholar_year.teaching_group.name,
                "time_period": obj.scholar_year.time_period.name,
                "study_plan": obj.scholar_year.study_plan.name,
                "semester": obj.scholar_year.semester.name,
            }
        return None

    class Meta:
        model = SubjectDescription
        fields = '__all__'


class TeachingAssignmentSerializer(ModelSerializer):
    professor_id = serializers.IntegerField(required=True, write_only=True)
    professor = serializers.SerializerMethodField()

    subject_description_id = serializers.IntegerField(
        required=True, write_only=True)
    subject_description = serializers.SerializerMethodField()

    def get_professor(self, obj) -> dict:
        if obj.professor:
            return {
                "id": obj.professor.id,
                "name": obj.professor.name,
                "last_name": obj.professor.last_name
            }
        return None

    def get_subject_description(self, obj) -> dict:
        if obj.subject_description:
            return {
                "id": obj.subject_description.id,
                "name": obj.subject_description.subject.name,
                "class_type": obj.subject_description.class_type.name,
                "time_period": obj.subject_description.time_period.name,
                "scholar_year": obj.subject_description.scholar_year.teaching_group.name,
                "number_of_hours": obj.subject_description.number_of_hours,
                "number_of_groups": obj.subject_description.number_of_groups

            }
        return None

    class Meta:
        model = TeachingAssignment
        fields = '__all__'


class CarmenTableSerializer(ModelSerializer):
    teaching_group_id = serializers.IntegerField(
        required=True, write_only=True)
    teaching_group = serializers.SerializerMethodField()

    time_period_id = serializers.IntegerField(
        required=True, write_only=True)
    time_period = serializers.SerializerMethodField()

    semester_id = serializers.IntegerField(
        required=True, write_only=True)
    semester = serializers.SerializerMethodField()

    study_plan_id = serializers.IntegerField(
        required=True, write_only=True)
    study_plan = serializers.SerializerMethodField()

    def get_teaching_group(self, obj) -> dict:
        if obj.teaching_group:
            return {
                "id": obj.teaching_group.id,
                "name": obj.teaching_group.name
            }
        return None

    def get_time_period(self, obj) -> dict:
        if obj.time_period:
            return {
                "id": obj.time_period.id,
                "name": obj.time_period.name
            }
        return None

    def get_semester(self, obj) -> dict:
        if obj.semester:
            return {
                "id": obj.semester.id,
                "name": obj.semester.name
            }
        return None

    def get_study_plan(self, obj) -> dict:
        if obj.study_plan:
            return {
                "id": obj.study_plan.id,
                "name": obj.study_plan.name
            }
        return None

    class Meta:
        model = CarmenTable
        fields = '__all__'


class TeachingPlanningSerializer(ModelSerializer):
    teaching_assignments = TeachingAssignmentSerializer(
        read_only=True, many=True)

    class Meta:
        model = TeachingPlanning
        fields = '__all__'

        # ----------- Thesis Committee ------------


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ThesisSerializer(ModelSerializer):
    tutor_id = serializers.IntegerField(required=True, write_only=True)
    tutor = serializers.SerializerMethodField()

    cotutor_id = serializers.IntegerField(required=True, write_only=True)
    cotutor = serializers.SerializerMethodField()

    student_id = serializers.IntegerField(required=True, write_only=True)
    student = serializers.SerializerMethodField()

    def get_tutor(self, obj) -> dict:
        if obj.tutor:
            return {
                "id": obj.tutor.id,
                "name": obj.tutor.name,
                "last_name": obj.tutor.last_name,
            }
        return None

    def get_cotutor(self, obj) -> dict:
        if obj.cotutor:
            return {
                "id": obj.cotutor.id,
                "name": obj.cotutor.name,
                "last_name": obj.cotutor.last_name,
            }
        return None

    def get_student(self, obj) -> dict:
        if obj.student:
            return {
                "id": obj.student.id,
                "name": obj.student.name,
                "last_name": obj.student.last_name,
            }
        return None

    class Meta:
        model = Thesis
        fields = '__all__'


class ThesisCommitteeSerializer(ModelSerializer):
    thesis_id = serializers.IntegerField(required=True, write_only=True)
    thesis = serializers.SerializerMethodField()

    opponent_id = serializers.IntegerField(required=True, write_only=True)
    opponent = serializers.SerializerMethodField()

    secretary_id = serializers.IntegerField(required=True, write_only=True)
    secretary = serializers.SerializerMethodField()

    def get_thesis(self, obj) -> dict:
        if obj.thesis:
            return {
                "id": obj.thesis.id,
                "title": obj.thesis.title,
                "student": obj.thesis.student.name + ' ' + obj.thesis.student.last_name,
                "tutor": obj.thesis.tutor.name + ' ' + obj.thesis.tutor.last_name,
                "cotutor": obj.thesis.cotutor.name + ' ' + obj.thesis.cotutor.last_name,
            }
        return None

    def get_opponent(self, obj) -> dict:
        if obj.opponent:
            return {
                "id": obj.opponent.id,
                "name": obj.opponent.name,
                "last_name": obj.secretary.last_name,
            }
        return None

    def get_secretary(self, obj) -> dict:
        if obj.secretary:
            return {
                "id": obj.secretary.id,
                "name": obj.secretary.name,
                "last_name": obj.secretary.last_name,
            }
        return None

    class Meta:
        model = ThesisCommittee
        fields = '__all__'
