"""Users models."""
# Python
# Django
from django.contrib.auth.models import User
from django.db import models
# Local Apps

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extends the base data with other
    information.
    fields:
    - user: OneToOneField
    - website: urlField
    - biography: text
    - phone: Char
    - picture
    """
    # Relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User fields
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    # Media fields
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    # Date fields
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns profile username"""
        return self.user.username