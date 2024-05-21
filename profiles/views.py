from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileListSerializer

# Create your views here.
class ProfilesListView(APIView):
  """
  A view to return a list of all profiles.
  """
  queryset = Profile.objects.all()
  serializer_class = ProfileListSerializer

  def get(self, request):
    profiles = Profile.objects.all()
    serializer = ProfileListSerializer(profiles, many=True)
    return Response(serializer.data)
  