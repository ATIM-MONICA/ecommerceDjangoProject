from django.db import models
from order.models import Order

# Create your models here.
class ReturnRequest(models.Model):
    order = models.ForeignKey(Order, related_name='returns', on_delete=models.CASCADE)
    reason = models.TextField()
    requested_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # e.g. 'Pending', 'Approved', 'Rejected'

    def __str__(self):
        return f"Return request for {self.order.order_number}"

