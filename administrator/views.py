from rest_framework import generics
from .models import Administrator
from .serializers import AdministratorSerializer
# Create your views here.
# List and create Administrator
class AdministratorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

# Retrieve, update, or delete a single Administrator
class AdministratorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

