from django.db.models import fields
from rest_framework import serializers
from .models import Note, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'category', 'text']
