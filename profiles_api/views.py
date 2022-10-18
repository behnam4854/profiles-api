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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


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


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handling user feed or every acton on feeds"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeeditem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )
    def perform_create(self, serializer):
        """asign the feed to the requested user """
        serializer.save(user_profile=self.request.user)
