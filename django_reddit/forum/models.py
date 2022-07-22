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
    # Many to one.
    vote_up = models.ManyToManyField(User, related_name='post_vote_up')

    def __str__(self) -> str:
        """Return the title field in a string."""
        return str(self.title)

    def __len__(self) -> int:
        """Return length of a post."""
        return len(self.content)

    def number_of_votes(self):
        """Count all likes of a post."""
        return self.vote_up.count()


class CommentPost(models.Model):
    """Post comment model."""
    # content
    content = models.TextField(blank=False)
    # Foreign key
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_up = models.ManyToManyField(User, related_name='comment_vote_up')
    # Meta
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string of the comment."""
        return str(self.content)[:50]
    
    def __len__(self) -> int:
        """Return length of a post."""
        return len(self.content)
