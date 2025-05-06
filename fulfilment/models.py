from django.db import models
from order.models import Order

# Create your models here.
class Fulfilment(models.Model):
    order = models.OneToOneField(Order, related_name='fulfilment', on_delete=models.CASCADE)
    fulfilled_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)  # e.g. 'Fulfilled', 'In Process', 'Delayed'

    def __str__(self):
        return f"Fulfilment for {self.order.order_number}"

