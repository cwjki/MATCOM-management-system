from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Note, Snippet


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code']
