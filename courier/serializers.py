from rest_framework import serializers
from .models import Courier

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'  # Serialize all fields from Courier model

