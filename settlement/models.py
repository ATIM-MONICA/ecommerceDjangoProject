from django.db import models
from vendor.models import Vendor

# Create your models here.
class Settlement(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='settlements', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    settlement_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # e.g. 'Pending', 'Completed'

    def __str__(self):
        return f"Settlement for {self.vendor.name} - {self.amount}"

