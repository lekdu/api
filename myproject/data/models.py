from django.db import models
from django.contrib.auth.models import User
import datetime

class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    
class Review(models.Model):
    rating = models.IntegerField()
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    ipAddress = models.CharField(max_length=15)
    date = models.DateField(default=datetime.date.today)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    reviewer = models.OneToOneField(User, on_delete=models.CASCADE)
    