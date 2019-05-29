from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from django.http import HttpResponse
# from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    # serializer = serializers.UserProfileSerializer(user1, many=True)
    def get(self, request):
        # queryset = models.ProfileFeedItem.objects.all()
        user1 = models.UserProfile.objects.all()
        serializer = serializers.HelloSerializer(user1, many=True)


    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})


class MasterProfileViewSet(viewsets.ModelViewSet):
    queryset = models.MasterProfile.objects.all()
    serializer_class = serializers.MasterProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('master_id',)
    # serializer = serializers.UserProfileSerializer(user1, many=True)
    def get(self, request):
        # queryset = models.ProfileFeedItem.objects.all()
        user1 = models.MasterProfile.objects.all()
        serializer = serializers.MasterProfileSerializer(user1, many=True)


    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
