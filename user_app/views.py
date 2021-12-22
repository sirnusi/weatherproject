from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
