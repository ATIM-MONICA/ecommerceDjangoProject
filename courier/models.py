from django.db import models

# Create your models here.
class Courier(models.Model):
    name = models.CharField(max_length=100)  # Courier company name
    tracking_url = models.URLField(blank=True, null=True)  # URL to track shipments

    def __str__(self):
        return self.name

