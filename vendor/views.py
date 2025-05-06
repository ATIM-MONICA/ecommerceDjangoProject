from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
# Create your views here.
# List and create Vendor
class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

# Retrieve, update, or delete a single Vendor
class VendorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
