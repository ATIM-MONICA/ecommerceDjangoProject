from rest_framework import generics
from .models import Delivery
from .serializers import DeliverySerializer
# Create your views here.
# List and create Delivery
class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

# Retrieve, update, or delete a single Delivery
class DeliveryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
