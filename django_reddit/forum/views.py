"""Views file"""
# Django
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Python
# Local
from .forms import PostForm, CommentForm
from .models import CommentPost, Post

# Views

class CreateCommentView(LoginRequiredMixin, CreateView):
    """Create a new Post.

    This view creates posts if the user is logged.
    """

    template_name: str = 'forum/new_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        context['profile'] = self.request.user.profile
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create posts."""
    template_name: str = 'forum/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class Feed(LoginRequiredMixin, ListView):
    """View to display all posts."""
    model = Post
    template_name: str = 'forum/feed.html'
    context_object_name: str = 'posts'

    def get_queryset(self):
        """Return the last five published question"""
        return Post.objects.filter(created__lte=timezone.now()).order_by('-created')


class PostDetail(LoginRequiredMixin, DetailView):
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
        data['comments'] = CommentPost.objects.filter(post__pk=likes_connected.pk)
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

    return HttpResponseRedirect(reverse('posts:detail', kwargs={'pk':pk}))
