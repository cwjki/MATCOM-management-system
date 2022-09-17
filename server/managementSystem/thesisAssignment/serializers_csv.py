from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Place, Keyword, Thesis, ThesisCommittee


class PlaceSerializerCSV(ModelSerializer):
    class Meta:
        model = Place
        exclude = ['id']


class KeywordSerializerCSV(ModelSerializer):
    class Meta:
        model = Keyword
        exclude = ['id']


class ThesisSerializerCSV(ModelSerializer):
    tutor = serializers.SerializerMethodField()
    cotutors = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()

    def get_tutor(self, obj) -> dict:
        if obj.tutor:
            return {
                "name": obj.tutor.name,
                "last_name": obj.tutor.last_name,
            }
        return None

    def get_cotutors(self, obj) -> dict:
        if obj.cotutors:
            data = []
            for tutor in obj.cotutors.all():
                data.append({
                    "name": tutor.name,
                    "last_name": tutor.last_name,
                })
            return data
        return None

    def get_keywords(self, obj) -> dict:
        if obj.keywords:
            data = []
            for keyword in obj.keywords.all():
                data.append({
                    "name": keyword.name,
                })
            return data
        return None

    class Meta:
        model = Thesis
        exclude = ['id']


class ThesisCommitteeSerializerCSV(ModelSerializer):
    opponent = serializers.SerializerMethodField()
    secretary = serializers.SerializerMethodField()
    president = serializers.SerializerMethodField()
    place = serializers.SerializerMethodField()
    thesis = serializers.SerializerMethodField()

    def get_thesis(self, obj) -> dict:
        if obj.thesis:
            return {
                "title": obj.thesis.title,
                "student": obj.thesis.student
            }
        return None

    def get_opponent(self, obj) -> dict:
        if obj.opponent:
            return {
                "name": obj.opponent.name,
                "last_name": obj.opponent.last_name
            }
        return None

    def get_secretary(self, obj) -> dict:
        if obj.secretary:
            return {
                "name": obj.secretary.name,
                "last_name": obj.secretary.last_name
            }
        return None

    def get_president(self, obj) -> dict:
        if obj.president:
            return {
                "name": obj.president.name,
                "last_name": obj.president.last_name
            }
        return None

    def get_place(self, obj) -> dict:
        if obj.place:
            return {
                "name": obj.place.name
            }
        return None

    class Meta:
        model = ThesisCommittee
        exclude = ['id']
