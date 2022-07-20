"""django_reddit URL Configuration"""
# Django
from django.urls import path
# Local
from .views import index


urlpatterns = [
    path('', index, name='index')
]
