from django.contrib.auth.models import User, Group
from .models import Review, Company
from rest_framework import serializers
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    reviewer = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        fields = ['title', 'summary','ipAddress','rating','company','reviewer']
        
