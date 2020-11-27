from django.urls import path, include
from rest_framework import routers

from api import views
from .views import CustomAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('token', CustomAuthToken.as_view(), name='token'),
    path('', include(router.urls)),
]
