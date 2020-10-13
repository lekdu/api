from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from data.serializers import ReviewSerializer
from .forms import ReviewForm
from .models import Review
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

    
@login_required
def new_review(request):
    if request.user is None:
       return redirect('/')
    form = ReviewForm()
    return render(request, 'form.html', {'form': form})