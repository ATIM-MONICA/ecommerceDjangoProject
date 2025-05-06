from rest_framework import generics
from .models import Settlement
from .serializers import SettlementSerializer
# Create your views here.
# List and create Settlement
class SettlementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer

# Retrieve, update, or delete a single Settlement
class SettlementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
