from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
  """
  A serializer to return a list of all profiles.
  """
  class Meta:
    model = Profile
    fields = ['id', 'owner', 'name', 'bio', 'image', 'followers']
    read_only_fields = ['owner', 'bio', 'followers']



  