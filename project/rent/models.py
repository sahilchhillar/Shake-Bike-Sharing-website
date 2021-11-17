from django.db import models

# Create your models here.
class RentTable(models.Model):
    userId = models.CharField(default=None, max_length=20)
    bikeId = models.IntegerField(default=None)
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    rentLocation = models.CharField(max_length=30, null=True)
    returnLocation = models.CharField(max_length=30, null=True)
    charges = models.FloatField(null=True)
    wallet_amount = models.FloatField(null=True)

    def __str__(self) -> str:
        return str(self.userId) + " " + str(self.bikeId)


