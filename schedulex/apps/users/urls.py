
from django.urls import path
from .views import CustomLoginView
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="token_obtain_pair"),
    
]
