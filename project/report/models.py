from django.db import models

# Create your models here.
class ReportBikes(models.Model):
    bikeId = models.IntegerField(null=True)
    message = models.CharField(max_length=100, null=True)
    status = models.BooleanField(null=True, default=True)
    pickup = models.CharField(max_length=100, null=True)
    drop = models.CharField(max_length=100, null=True)
    
