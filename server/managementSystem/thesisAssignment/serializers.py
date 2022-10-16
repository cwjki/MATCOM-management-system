from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from teachingAssignment.serializers import ProfessorSerializer
from .models import Keyword, Place, Thesis, ThesisCommittee, ThesisDefense


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class KeywordSerializer(ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class ThesisSerializer(ModelSerializer):
    tutor_id = serializers.IntegerField(required=True, write_only=True)
    tutor = serializers.SerializerMethodField()

    cotutors = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()

    def get_tutor(self, obj) -> dict:
        if obj.tutor:
            return {
                "id": obj.tutor.id,
                "name": obj.tutor.name,
                "last_name": obj.tutor.last_name,
            }
        return None

    def get_cotutors(self, obj) -> dict:
        if obj.cotutors:
            data = []
            for tutor in obj.cotutors.all():
                data.append({
                    "id": tutor.id,
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
                    "id": keyword.id,
                    "name": keyword.name,
                })
            return data
        return None

    class Meta:
        model = Thesis
        fields = '__all__'


class ThesisCommitteeSerializer(ModelSerializer):
    # thesis_id = serializers.IntegerField(required=True, write_only=True)
    # thesis = serializers.SerializerMethodField()

    opponent_id = serializers.IntegerField(required=True, write_only=True)
    opponent = serializers.SerializerMethodField()

    secretary_id = serializers.IntegerField(required=True, write_only=True)
    secretary = serializers.SerializerMethodField()

    president_id = serializers.IntegerField(required=True, write_only=True)
    president = serializers.SerializerMethodField()

    thesis_id = serializers.IntegerField(required=True, write_only=True)
    thesis = serializers.SerializerMethodField()

    def get_thesis(self, obj) -> dict:
        if obj.thesis:

            cotutors = ''
            for cotutor in obj.thesis.cotutors.all():
                cotutors += cotutor.name + ' ' + cotutor.last_name + ', '
            cotutors = cotutors[0: -2]

            keywords = ''
            for keyword in obj.thesis.keywords.all():
                keywords += keyword.name + ', '
            keywords = keywords[0: -2]

            return {
                "id": obj.thesis.id,
                "title": obj.thesis.title,
                "student": obj.thesis.student,
                "tutor": obj.thesis.tutor.name + ' ' + obj.thesis.tutor.last_name,
                "cotutors": cotutors,
                "keywords": keywords
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

    class Meta:
        model = ThesisCommittee
        fields = '__all__'


class ThesisDefenseSerializer(ModelSerializer):

    thesis_committee_id = serializers.IntegerField(
        required=True, write_only=True)
    thesis_committee = serializers.SerializerMethodField()

    place_id = serializers.IntegerField(required=True, write_only=True)
    place = serializers.SerializerMethodField()

    def get_thesis_committee(self, obj) -> dict:
        if obj.thesis_committee:

            keywords = ''
            for keyword in obj.thesis_committee.thesis.keywords.all():
                keywords += keyword.name + ', '
            keywords = keywords[0: -2]

            cotutors = ''
            for cotutor in obj.thesis_committee.thesis.cotutors.all():
                cotutors += cotutor.name + ' ' + cotutor.last_name + ', '
            cotutors = cotutors[0: -2]

            return {
                "id": obj.thesis_committee.id,
                "secretary": obj.thesis_committee.secretary.name + ' ' + obj.thesis_committee.secretary.last_name,
                "president": obj.thesis_committee.president.name + ' ' + obj.thesis_committee.president.last_name,
                "opponent": obj.thesis_committee.opponent.name + ' ' + obj.thesis_committee.opponent.last_name,
                "tutor": obj.thesis_committee.thesis.tutor.name + ' ' + obj.thesis_committee.thesis.tutor.last_name,
                "thesis_title": obj.thesis_committee.thesis.title,
                "student": obj.thesis_committee.thesis.student,
                "cotutors": cotutors,
                "keywords": keywords
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
        model = ThesisDefense
        fields = '__all__'
