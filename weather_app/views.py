from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
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

    # def get_queryset(self):
    #     my_notes = Note.objects.filter(owner=self.request.user)
    #     return my_notes                

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
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Note.objects.filter(owner__username=username)    