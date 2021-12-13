from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from .permissions import NotePermission
# Create your views here.

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
    
class NoteList(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NotePermission]
    filter_backends = [DjangoFilterBackend] #filter by the fields in our models.py in your url
    filterset_fields = ['category__name', 'owner__username']#the exact same word as it is on the database.

    # def get_queryset(self):
    #     my_notes = Note.objects.filter(owner=self.request.user)
    #     return my_notes                

class NoteSearch(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category__name']
    
class NoteCreate(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [NotePermission]
         
class NoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NotePermission]

#filter the list by username in the database. 
class UserNote(ListAPIView):
    serializer_class = NoteSerializer
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Note.objects.filter(owner__username=username)    
    
    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Note.objects.filter(owner__username=username)    