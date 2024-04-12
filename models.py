from django.db import models
from datetime import datetime


class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    phone=models.IntegerField()

class Confirm(models.Model):
    pickupLocation = models.CharField(max_length=100)
    dropoffLocation= models.CharField(max_length=100)
    pickupDate = models.DateTimeField()
    dropoffDate = models.DateTimeField()
    cartype = models.CharField(max_length=100)


