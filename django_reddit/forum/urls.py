"""django_reddit URL Configuration"""
# Django
from django.urls import path
# Local
from .views import Feed, PostDetail, PostVoteUp


app_name = 'posts'
urlpatterns = [
    path('', Feed.as_view(), name='feed'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('posts/<int:pk>/vote_up/', PostVoteUp, name='vote_up')
]
