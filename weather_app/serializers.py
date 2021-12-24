from rest_framework import serializers
from .models import Note, Category

class NoteSerializer(serializers.ModelSerializer):
    #owner = serializers.StringRelatedField(read_only=True)
    # category = serializers.CharField(source='category.name')
    
    class Meta:
        model = Note
        fields = "__all__"
        

class CategorySerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
   
    
    class Meta:
        model = Category
        fields = "__all__"

