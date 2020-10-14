from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from data.serializers import ReviewSerializer
from .forms import ReviewForm
from .models import Review, Company
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import socket
import requests

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Review.objects.all()
        else:
            return Review.objects.all().filter(reviewer=user)

class ReviewSave(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        data = self.request.POST
        user = self.request.user
        ip = socket.gethostbyname(socket.gethostname())
        company = Company.objects.filter(id=data.get("company")).first();
        rev = Review(title=data.get("title"),summary=data.get("summary"),ipAddress=ip,reviewer=user,company=company,rating=data.get("rating"))
        rev.save()
        r = Review.objects.filter(id=rev.id);
        return r

    
@login_required
def new_review(request):
    if request.method == 'POST':
        host = socket.gethostname()
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        r = requests.get("http://localhost:8000/reviewsSave/",data=request.POST,headers={'Authorization': "Token "+str(token)})
    form = ReviewForm()
    return render(request, 'form.html', {'form': form})