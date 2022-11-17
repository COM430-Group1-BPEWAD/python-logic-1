from django.db import models

# Create your models here.
class doctor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

class patient(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    allergies = models.CharField(max_length=60)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)