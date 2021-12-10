from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from .permissions import NotePermission
# Create your views here.

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class NoteList(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [NotePermission]
    
    
class NoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [NotePermission]