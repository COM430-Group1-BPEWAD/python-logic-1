from django.db import models

# Create your models here.
class doctor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

class patient(models.Model):
    patientUserName = models.CharField(max_length=30, default="nope")
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=120, default="nope@nope.nope")
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    allergies = models.CharField(max_length=60)
    #doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, default=0)

class bpReadings(models.Model):
    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    diastolic = models.IntegerField()
    systolic = models.IntegerField()