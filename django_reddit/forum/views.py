"""Views file"""
# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Python
# Local
from .models import Post

# Views

class Feed(ListView):
    """View to display all posts."""
    model = Post
    template_name: str = 'forum/feed.html'
    context_object_name: str = 'posts'

    def get_queryset(self):
        """Return the last five published question"""
        return Post.objects.filter(created__lte=timezone.now()).order_by('-created')


class PostDetail(DetailView):
    """View to display details from a post."""
    model = Post
    template_name: str = 'forum/detail_post.html'
