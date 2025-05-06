from rest_framework import generics
from .models import Fulfilment
from .serializers import FulfilmentSerializer
# Create your views here.
# List and create Fulfilment
class FulfilmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fulfilment.objects.all()
    serializer_class = FulfilmentSerializer

# Retrieve, update, or delete a single Fulfilment
class FulfilmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fulfilment.objects.all()
    serializer_class = FulfilmentSerializer