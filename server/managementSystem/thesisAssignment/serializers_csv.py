from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Place, Keyword, Thesis, ThesisCommittee, ThesisDefense


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
    thesis = serializers.SerializerMethodField()

    def get_thesis(self, obj) -> dict:
        if obj.thesis:
            tutors = [obj.thesis.tutor.name + ' ' + obj.thesis.tutor.last_name]
            for cotutor in obj.thesis.cotutors.all():
                tutors.append(cotutor.name + ' ' + cotutor.last_name)
            keywords = [keyword.name for keyword in obj.thesis.keywords.all()]
            return {
                "title": obj.thesis.title,
                "student": obj.thesis.student,
                "tutors": tutors,
                "keywords": keywords
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

    class Meta:
        model = ThesisCommittee
        exclude = ['id']


class ThesisDefenseSerializerCSV(ModelSerializer):
    thesis_committee = serializers.SerializerMethodField()
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
                "name": obj.place.name
            }
        return None

    class Meta:
        model = ThesisDefense
        exclude = ['id']
