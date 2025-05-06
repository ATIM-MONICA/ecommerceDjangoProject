from rest_framework import generics
from .models import ReturnRequest
from .serializers import ReturnRequestSerializer
# Create your views here.
# List and create ReturnRequest
class ReturnRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReturnRequest.objects.all()
    serializer_class = ReturnRequestSerializer

# Retrieve, update, or delete a single ReturnRequest
class ReturnRequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReturnRequest.objects.all()
    serializer_class = ReturnRequestSerializer