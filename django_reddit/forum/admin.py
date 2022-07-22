#form app admin configuration.

# Django
from typing import List
from django.contrib import admin
# Models.
from .models import CommentPost, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin class."""

    fieldsets = (
        (
            'Post', {
                'fields': (('title', 'content'),)
            }
        ),
        (
            'User Information', {
                'fields': (
                    ('user'),
                    ('profile'),
                )
            }
        ),
        (
            'Metadata', {
                'fields': (('created', 'updated'),)
            }
        )
    )

    list_display: set = ('pk', 'title', 'content', 'user')
    readonly_fields: set = ('created', 'updated')
    search_fields: List[str] = (
        'user__username',
        'title',
        'pk',
    )
    list_filter: List[str] = (
        'created',
        'updated',
    )

admin.site.register(CommentPost)
