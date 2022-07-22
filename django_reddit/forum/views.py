"""Views file"""
# Django
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.vote_up.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_votes()
        data['post_is_liked'] = liked
        return data


@login_required
def PostVoteUp(request, pk):
    """Post like view.
    
    This function validate if a user didn't like a post and like it or dislike it.
    """
    post = get_object_or_404(Post, id=pk)
    if post.vote_up.filter(id=request.user.id).exists():
        post.vote_up.remove(request.user)
    else:
        post.vote_up.add(request.user)

    return HttpResponseRedirect(reverse('posts:detail', args=[str(pk)]))