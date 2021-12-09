from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Note
from .serializers import NoteSerializer
from .permissions import NotePermission
# Create your views here.
class NoteList(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [NotePermission]
    
    
class NoteDetail(RetrieveUpdateDestroyAPIView):
    pass