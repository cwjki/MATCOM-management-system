from asyncore import read
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from teachingAssignment.serializers import ProfessorSerializer, ScholarYearSerializer

from teachingAssignment.models import Professor

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
    tutor = ProfessorSerializer(read_only=True)

    cotutors_id = serializers.PrimaryKeyRelatedField(
        required=False, many=True, read_only=False, queryset=Professor.objects.all(), source='cotutors')
    cotutors = ProfessorSerializer(many=True, read_only=True)

    keywords_id = serializers.PrimaryKeyRelatedField(
        required=False, many=True, read_only=False, queryset=Keyword.objects.all(), source='keywords')
    keywords = KeywordSerializer(many=True, read_only=True)

    scholar_year_id = serializers.IntegerField(required=True, write_only=True)
    scholar_year = ScholarYearSerializer(read_only=True)

    def create(self, validated_data):
        cotutors = validated_data.pop(
            'cotutors') if 'cotutors' in validated_data else []
        keywords = validated_data.pop('keywords')

        thesis = Thesis.objects.create(
            **validated_data)

        for cotutor in cotutors:
            thesis.cotutors.add(cotutor)

        for keyword in keywords:
            thesis.keywords.add(keyword)

        thesis_committee = ThesisCommittee.objects.create(thesis_id=thesis.id)
        ThesisDefense.objects.create(thesis_committee_id=thesis_committee.id)
        return thesis

    class Meta:
        model = Thesis
        fields = '__all__'


class ThesisCommitteeSerializer(ModelSerializer):
    opponent_id = serializers.IntegerField(required=True, write_only=True)
    opponent = ProfessorSerializer(read_only=True)

    president_id = serializers.IntegerField(required=True, write_only=True)
    president = ProfessorSerializer(read_only=True)

    thesis_id = serializers.IntegerField(required=True, write_only=True)
    thesis = ThesisSerializer(read_only=True)

    # secretary_id = serializers.IntegerField(write_only=True)
    # secretary = ProfessorSerializer(read_only=True)

    class Meta:
        model = ThesisCommittee
        fields = '__all__'


class ThesisDefenseSerializer(ModelSerializer):

    thesis_committee_id = serializers.IntegerField(
        required=True, write_only=True)
    thesis_committee = ThesisCommitteeSerializer(read_only=True)

    place_id = serializers.IntegerField(required=True, write_only=True)
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = ThesisDefense
        fields = '__all__'
