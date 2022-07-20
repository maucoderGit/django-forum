"""django_reddit URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # FORUM
    path('', include('forum.urls'))
    # USERS
]
