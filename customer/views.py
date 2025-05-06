from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

# List and create Customers
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Retrieve, update, or delete a specific Customer
class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

