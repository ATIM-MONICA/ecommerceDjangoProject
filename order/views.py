from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
# Create your views here.
# List and create Order
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Retrieve, update, or delete a single Order
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
