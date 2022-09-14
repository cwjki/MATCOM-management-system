from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Student, Thesis, ThesisCommittee


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
