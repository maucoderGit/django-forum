"""django_reddit URL Configuration"""
# Django
from django.urls import path
# Local
from .views import Feed, PostDetail


app_name = 'posts'
urlpatterns = [
    path('', Feed.as_view(), name='feed'),
    path('posts/<int:pk>', PostDetail.as_view(), name='detail'),
]
