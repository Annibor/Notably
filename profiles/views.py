from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class ProfilesListView(ListAPIView):
  """
  A view to return a list of all profiles.
  """
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['name', 'bio']
  search_fields = ['name', 'bio']  
  

class ProfileDetailView(APIView):
  """
  A view to return a single profile.
  """

  serializer_class = ProfileSerializer

  def get(self, request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)