from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from teachingAssignment.serializers import ProfessorSerializer
from .models import Place, Thesis, ThesisCommittee


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ThesisSerializer(ModelSerializer):
    tutors = serializers.SerializerMethodField()

    cotutor_id = serializers.IntegerField(required=True, write_only=True)
    cotutor = serializers.SerializerMethodField()

    def get_tutors(self, obj) -> dict:
        if obj.tutors:
            data = []
            for tutor in obj.tutors.all():
                data.append({
                    "id": tutor.id,
                    "name": tutor.name,
                    "last_name": tutor.last_name,
                })
            return data
        return None

    def get_cotutor(self, obj) -> dict:
        if obj.cotutor:
            return {
                "id": obj.cotutor.id,
                "name": obj.cotutor.name,
                "last_name": obj.cotutor.last_name,
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

    president_id = serializers.IntegerField(required=True, write_only=True)
    president = serializers.SerializerMethodField()

    place_id = serializers.IntegerField(required=True, write_only=True)
    place = serializers.SerializerMethodField()

    def get_thesis(self, obj) -> dict:
        if obj.thesis:
            return {
                "id": obj.thesis.id,
                "title": obj.thesis.title,
                "student": obj.thesis.student,
                "tutor": obj.thesis.tutor.name + ' ' + obj.thesis.tutor.last_name,
                "cotutor": obj.thesis.cotutor.name + ' ' + obj.thesis.cotutor.last_name
            }
        return None

    def get_opponent(self, obj) -> dict:
        if obj.opponent:
            return {
                "id": obj.opponent.id,
                "name": obj.opponent.name,
                "last_name": obj.opponent.last_name
            }
        return None

    def get_secretary(self, obj) -> dict:
        if obj.secretary:
            return {
                "id": obj.secretary.id,
                "name": obj.secretary.name,
                "last_name": obj.secretary.last_name
            }
        return None

    def get_president(self, obj) -> dict:
        if obj.president:
            return {
                "id": obj.president.id,
                "name": obj.president.name,
                "last_name": obj.president.last_name
            }
        return None

    def get_place(self, obj) -> dict:
        if obj.place:
            return {
                "id": obj.place.id,
                "name": obj.place.name
            }
        return None

    class Meta:
        model = ThesisCommittee
        fields = '__all__'
