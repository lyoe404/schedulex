
from django.urls import path
from .views import login_view, schedule_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("auth/", include("users.urls")),
    path('login/', login_view),
    path('generate/', schedule_view),
    path("admin/", admin.site.urls),
]
