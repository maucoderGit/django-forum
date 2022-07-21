"""Forum tests file."""

# Django
from datetime import datetime
from django.test import TestCase

# Local
from .models import Post
from users.models import Profile, User

# Models to test

def create_post(
        title: str = 'title',
        user: User = User(),
        profile: Profile = Profile(),
        content: str = 'Lorem ipsum',
        time: datetime = None
    ) -> Post:
    """Create post.
    
    Create a post instance to verify fields and validate if it's working sucessfully.
    
    fields:
    - title: CharField
    - user_id: foreign key of User model
    - profile_id: foreign key of Profile model
    - content: TextField

    Returns a Post instance to test.
    """
    post = Post(title=title, user=user, profile=profile, content=content, created=time)
    
    return post

# MODELS Tests


class PostTest(TestCase):
    """Posts tests
    
    Test and validations to verify correctly working of the posts models."""
    
    def test_post_instance_created_sucessfully(self):
        """Validate is a post instance is generated sucessfully without exceptions."""
        post = create_post()
        self.assertIsInstance(post ,Post)
    
    def test_post_instance_returns_title(self):
        """The post objects must returns the title in string format."""
        post = create_post()
        self.assertIsInstance(post.title, str, msg='The title is not equals to a string.')
        self.assertIsInstance(post.user, User)
        self.assertIsInstance(post.profile, Profile)
        self.assertIsInstance(post.content, str)

    def test_return_length_from_post_content(self):
        """The post content could be returned in a integer number."""
        post = create_post()
        self.assertIsInstance(len(post), int)
        self.assertEquals(len(post), len(post.content))
