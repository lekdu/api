
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from data import views

'''
DEVELOPED BY EDUARDO CABEZAS
14/10/2020
'''

router = routers.DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='Review')
router.register(r'reviewsSave', views.ReviewSave, basename='ReviewSave')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('review/new/', views.new_review, name='new_review'),
]
