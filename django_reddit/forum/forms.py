"""Users app forms."""

# Django
from django import forms

# Models
from .models import Post, CommentPost


class CommentForm(forms.ModelForm):
    """Comment form generated automaticaly."""

    class Meta:
        """Form settings."""
        model = CommentPost
        fields = (
            'profile',
            'post',
            'content'
        )


class PostForm(forms.ModelForm):
    """Post form generated automaticaly."""

    class Meta:
        """Form settings."""
        model = Post
        fields = (
            'user',
            'profile',
            'title',
            'content'
        )