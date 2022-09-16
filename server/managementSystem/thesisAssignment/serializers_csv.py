from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Place, Keyword


class PlaceSerializerCSV(ModelSerializer):
    class Meta:
        model = Place
        exclude = ['id']


class KeywordSerializerCSV(ModelSerializer):
    class Meta:
        model = Keyword
        exclude = ['id']
