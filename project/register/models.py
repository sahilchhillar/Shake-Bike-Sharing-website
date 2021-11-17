from django.db import models

# Create your models here.
class Balance(models.Model):
    username = models.CharField(max_length=10)
    amount = models.FloatField(default=0.0, null=False)


