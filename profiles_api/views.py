from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers




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
        
            
