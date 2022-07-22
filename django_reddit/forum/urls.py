"""django_reddit URL Configuration"""
# Django
from django.urls import path
# Local
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.Feed.as_view(), name='feed'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('posts/<int:pk>/vote_up/', views.PostVoteUp, name='vote_up'),
    path('posts/create/', views.CreatePostView.as_view(), name='create'),
    path('posts/<int:pk>/comment/', views.CreateCommentView.as_view(), name='comment')
]
