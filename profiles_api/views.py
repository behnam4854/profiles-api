from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class HelloApiView(APIView):
    """test for seeing api views"""
    def get(self, request, format=None):
        """return some things """
        return Response("yay you have done what you use to do before")


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class UserLoginApiView(ObtainAuthToken):
    """for handling user authenthication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
