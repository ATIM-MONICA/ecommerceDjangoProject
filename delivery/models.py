from django.db import models
from order.models import Order
from courier.models import Courier

# Create your models here.
class Delivery(models.Model):
    order = models.OneToOneField(Order, related_name='delivery', on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)
    tracking_number = models.CharField(max_length=100)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)  # e.g. 'Out for delivery', 'Delivered'

    def __str__(self):
        return f"Delivery for {self.order.order_number}"

