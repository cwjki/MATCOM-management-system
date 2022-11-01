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


# class StudentSerializer(ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'


# class ThesisSerializer(ModelSerializer):
#     tutor_id = serializers.IntegerField(required=True, write_only=True)
#     tutor = serializers.SerializerMethodField()

#     cotutor_id = serializers.IntegerField(required=True, write_only=True)
#     cotutor = serializers.SerializerMethodField()

#     student_id = serializers.IntegerField(required=True, write_only=True)
#     student = serializers.SerializerMethodField()

#     def get_tutor(self, obj) -> dict:
#         if obj.tutor:
#             return {
#                 "id": obj.tutor.id,
#                 "name": obj.tutor.name,
#                 "last_name": obj.tutor.last_name,
#             }
#         return None

#     def get_cotutor(self, obj) -> dict:
#         if obj.cotutor:
#             return {
#                 "id": obj.cotutor.id,
#                 "name": obj.cotutor.name,
#                 "last_name": obj.cotutor.last_name,
#             }
#         return None

#     def get_student(self, obj) -> dict:
#         if obj.student:
#             return {
#                 "id": obj.student.id,
#                 "name": obj.student.name,
#                 "last_name": obj.student.last_name,
#             }
#         return None

#     class Meta:
#         model = Thesis
#         fields = '__all__'


# class ThesisCommitteeSerializer(ModelSerializer):
#     thesis_id = serializers.IntegerField(required=True, write_only=True)
#     thesis = serializers.SerializerMethodField()

#     opponent_id = serializers.IntegerField(required=True, write_only=True)
#     opponent = serializers.SerializerMethodField()

#     secretary_id = serializers.IntegerField(required=True, write_only=True)
#     secretary = serializers.SerializerMethodField()

#     def get_thesis(self, obj) -> dict:
#         if obj.thesis:
#             return {
#                 "id": obj.thesis.id,
#                 "title": obj.thesis.title,
#                 "student": obj.thesis.student.name + ' ' + obj.thesis.student.last_name,
#                 "tutor": obj.thesis.tutor.name + ' ' + obj.thesis.tutor.last_name,
#                 "cotutor": obj.thesis.cotutor.name + ' ' + obj.thesis.cotutor.last_name,
#             }
#         return None

#     def get_opponent(self, obj) -> dict:
#         if obj.opponent:
#             return {
#                 "id": obj.opponent.id,
#                 "name": obj.opponent.name,
#                 "last_name": obj.secretary.last_name,
#             }
#         return None

#     def get_secretary(self, obj) -> dict:
#         if obj.secretary:
#             return {
#                 "id": obj.secretary.id,
#                 "name": obj.secretary.name,
#                 "last_name": obj.secretary.last_name,
#             }
#         return None

#     class Meta:
#         model = ThesisCommittee
#         fields = '__all__'
