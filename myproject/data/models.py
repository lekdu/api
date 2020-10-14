from django.db import models
from django.contrib.auth.models import User
import datetime

'''
DEVELOPED BY EDUARDO CABEZAS
14/10/2020
'''

'''
Company model
'''
class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s" % self.name
    
'''
User Review Model
'''
class Review(models.Model):
    rating = models.IntegerField()
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    ipAddress = models.CharField(max_length=15)
    date = models.DateTimeField(default=datetime.datetime.now())
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1, related_name="company")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="reviewer")
    