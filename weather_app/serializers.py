from django.db.models import fields
from rest_framework import serializers
from .models import Note, Category

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = "__all__"

