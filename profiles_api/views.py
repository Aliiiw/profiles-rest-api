from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Api testing class"""
    
    def get(self, request, format = None):
        api_view = [
            'Uses Api functions',
            'like Djagno views',
            'control on logic',
            'handeled URLs ',
        ]
        return Response({'message' : 'Hello!','an_api': api_view})
    
    
