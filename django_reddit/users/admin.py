"""User admin files."""
# Django
from typing import Optional, Sequence
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin class."""
    fieldsets = (
        (
            'Profile', {
                'fields': tuple(('user', 'picture'))
            }
        ),
        (
            'Extra information', {
                'fields': (
                    ('website', 'phone_number'),
                    ('biography')
                )
            }
        ),
        (
            'Metadata', {
                'fields': tuple(('created', 'modified'))
            }
        )
    )
    readonly_fields = (
        'created',
        'modified',
        'user'
    )
    list_display = ('pk', 'user', 'phone_number', 'website')
    list_display_links = ('pk', 'user', 'website')
    list_editable = (
    
    )
    search_fields: Sequence[str] = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__pk',
        'user__username'
    )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

class ProfileInline(admin.StackedInline):
    """Profile inline.
    
    Enable possibility to edit and create user's profile."""
    model = Profile
    can_delete: bool = False
    verbose_name_plural: Optional[str] = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Enable profile admin fields.
    
    Enable to an admin the possibility to create and modify an profile
    frmm a user admin site.
    """
    inlines: Sequence = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)