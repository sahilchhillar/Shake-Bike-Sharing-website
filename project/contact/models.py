from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=500)