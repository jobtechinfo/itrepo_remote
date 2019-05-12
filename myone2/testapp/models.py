from django.db import models
from django.utils import timezone

# Create your models here.
class jobs(models.Model):
    date=models.DateTimeField(default=timezone.now)
    company=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    addr=models.CharField(max_length=30)
    email=models.EmailField()

class hydjobs(models.Model):
    date=models.DateTimeField(default=timezone.now)
    company=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    addr=models.CharField(max_length=30)
    email=models.EmailField()
    number=models.IntegerField()

class bngljobs(models.Model):
    date=models.DateTimeField(default=timezone.now)
    company=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    addr=models.CharField(max_length=30)
    email=models.EmailField()
    number=models.IntegerField()
