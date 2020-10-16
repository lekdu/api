
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from data import views

'''
DEVELOPED BY EDUARDO CABEZAS
14/10/2020
'''
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='Review')
router.register(r'reviewsF', views.ReviewFilterViewSet, basename='ReviewF')
router.register(r'reviewsSave', views.ReviewSave, basename='ReviewSave')


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.ini, name="ini"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('review/my/', views.myReviews, name='myreviews'),
    path('review/new/', views.new_review, name='new_review'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('logout', views.logout),
]

