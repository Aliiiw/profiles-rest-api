from http import HTTPStatus
import imp
from django import views
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class HelloApiView(APIView):
    """ Api testing class"""
    serializers_class = serializers.HelloSerializers
    
    
    def get(self, request, format=None):
        api_view = [
            'Uses Api functions',
            'like Djagno views',
            'control on logic',
            'handeled URLs ',
        ]
        return Response({'message' : 'Hello!','an_api': api_view})
    
    
    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    def put(self, request, pk=None):             #update
        return Response({'method' : 'put'})
    
    
    def patch(self, request, pk=None):          #update specific field
        return Response({'method' : 'patch'})
    
    
    def delete(self, request, pk=None):
        return Response({'method' : 'delete'})
        
            
class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializers
    
    def list(self, request):
        
        api_viewSet = [
            'Uses Api actions',
            'auto map urls',
            'more functionality less code',
        ]
        return Response({'viewSet' : api_viewSet})
    
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            
            return Response({'message' : message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        return Response({'method' : 'Get'})
    
    
    def update(self, request, pk=None):
        return Response({'method' : 'Put'})
    
    
    def partial_update(self, request, pk=None):
        return Response({'method' : 'Patch'})
    
    
    def destroy(self, request, pk=None):
        return Response({'method' : 'Delete'})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    