from rest_framework import serializers
from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'owner', 'name', 'bio', 'email', 'image', 'followers']
    read_only_fields = ['owner', 'bio', 'followers']



  