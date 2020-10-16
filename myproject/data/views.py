from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from data.serializers import ReviewSerializer
from .forms import ReviewForm
from .models import Review, Company
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import socket
import requests
import coreapi
import coreschema
from rest_framework import schemas
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, login, logout as do_logout
import json
'''
DEVELOPED BY EDUARDO CABEZAS
14/10/2020
'''


'''
API THAT SHOWS ONLY USER REVIEWS
REQUIRES USER TOKEN AUTHENTICATION
IF USER IS SUPER USER, IT WILL SHOW ALL REVIEWS
'''
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Review.objects.all()
        else:
            return Review.objects.all().filter(reviewer=user)

'''
API THAT SAVES A NEW REVIEW
REQUIRES USER TOKEN AUTHENTICATION
'''
class ReviewSave(viewsets.ModelViewSet):
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

    
'''
SHOW NEW REVIEW FORM
'''
@login_required
def new_review(request):
    if request.method == 'POST':
        host = socket.gethostname()
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        r = requests.get("http://localhost:8000/api/reviewsSave/",data=request.POST,headers={'Authorization': "Token "+str(token)})
    form = ReviewForm()
    return render(request, 'form.html', {'form': form})
    
def ini(request):
    if request.user.is_authenticated:
        return redirect("/review/new/")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/review/new/")
    return render(request, 'login.html')

def myReviews(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect("/")
    token, created = Token.objects.get_or_create(user=user)
    r = requests.get("http://localhost:8000/api/reviews/",headers={'Authorization': "Token "+str(token)})
    print(r)
    return render(request, 'myreviews.html', {'reviews':''})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')