from django.db import models
from django.contrib.auth.models import AbstractUser

"Based on https://www.youtube.com/watch?v=BTdcjOzfwCA User & profile model."
class User(AbstractUser):
  """
  Custom User model where email is the primary identifier for authentication
  instead of the username. The username is still used and required upon registration,
  but users log in using their email address.

  Attributes:
    username (models.CharField): The user's username, unique, used for identification.
    email (models.EmailField): The user's email address, unique, used for logging in.
    
  Constants:
    USERNAME_FIELD (str): Specifies the name of the field on the user model that is used as the unique identifier.
    REQUIRED_FIELDS (list): Specifies the names of the fields that will be prompted for when creating a user viat createsuperuser management command.
   """

  username = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.email