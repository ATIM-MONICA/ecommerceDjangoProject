from rest_framework import generics
from .models import Courier
from .serializers import CourierSerializer
# Create your views here.
# List and create Couriers
class CourierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

# Retrieve, update, or delete a single Courier
class CourierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

