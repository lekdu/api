from django.contrib.auth.models import User, Group
from .models import Review, Company
from rest_framework import serializers
from django.contrib.auth.models import User

'''
DEVELOPED BY EDUARDO CABEZAS
14/10/2020
'''

'''
COMPANY MODEL SERIALIZER
ITS REQUIRED ON REVIEW SERIALIZER
'''
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        ReadOnlyField = ['name', 'address', 'phone']

'''
USER MODEL SERIALIZER
ITS REQUIRED ON REVIEW SERIALIZER
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ReadOnlyField = ['username', 'email']

'''
USER REVIEW SERIALIZER
'''
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    reviewer = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        ReadOnlyField = ['title', 'summary','ipAddress','rating','company','reviewer','date']
        
