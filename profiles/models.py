from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Profile & create_profile are Based on Code Institutes walkthrough project: Moments.

class Profile(models.Model):
  """
  Extends the base User model to store additional personal information about users.

  Attributes:
    owner (OneToOneField): A one-to-one link to Django's built-in User model, ensuring
        that each user has one associated profile.
    name (CharField): The name of the profile, derived initially from the username of the user.
    bio (TextField): Additional content or description about the user, optional.
    image (ImageField): A profile image, with a default image if none is uploaded.
    followers (ManyToManyField): A many-to-many relationship allowing users to follow each other.

  Meta:
    ordering: ['-created_at']  # Orders profiles by their creation date, descending.
  """

  owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  name = models.CharField(max_length=35)
  bio = models.TextField(blank=True)
  email = models.EmailField(blank=True)
  image = models.ImageField(upload_to="images/", default="images/default.jpg")
  followers = models.ManyToManyField(
      User, related_name="followed_profiles", blank=True
  )
  
  class Meta:
    verbose_name = 'User Profile'
    verbose_name_plural = 'User Profiles'

  def __str__(self):
    return f"{self.owner.username}'s Profile"
  

def create_profile(sender, instance, created, **kwargs):
  """
  Creates a Profile for each new User created.
  """
  if created:
    Profile.objects.create(owner=instance, name=instance.username)
    

# Connects the create_profile function to the User model's post_save signal.
models.signals.post_save.connect(create_profile, sender=User)