from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer

# Create your views here.
class ProfilesListView(APIView):
  """
  A view to return a list of all profiles.
  """
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

  def get(self, request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
  

class ProfileDetailView(APIView):
  """
  A view to return a single profile.
  """

  serializer_class = ProfileSerializer

  def get(self, request, id):
    profile = get_object_or_404(Profile, id=id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)