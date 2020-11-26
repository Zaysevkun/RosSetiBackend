from django.urls import path, include
from .views import CustomAuthToken

urlpatterns = [
    path('token/', CustomAuthToken.as_view(), name='token'),
]
