"""Django models file"""

# Django
from django.db import models
from django.contrib.auth.models import User


# Models
class Post(models.Model):
    """Post model definition
    
    fields:
    - post_title. CHARFIELD
    - user_id. FK
    - post_content. TEXT
    - created
    - updated
    """
    # Data
    title = models.CharField(max_length=240)
    content = models.TextField(blank=False)
    # Meta
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)

    def __str__(self):
        """Return the title field in a string."""
        return str(self.title)
