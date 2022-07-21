"""Django models file"""

# Django
from django.db import models
from django.contrib.auth.models import User


# Models
class Post(models.Model):
    """Post model definition
    
    fields:
    - title. CHARFIELD
    - user_id. FK
    - profile_id
    - post_content. TEXT
    - created: Datetime field
    - updated: datetime field
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

    def __str__(self) -> str:
        """Return the title field in a string."""
        return str(self.title)

    def __len__(self) -> int:
        """Return length of a post."""
        return len(self.content)
