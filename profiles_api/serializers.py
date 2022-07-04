from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """ Serializers for api """
    
    name = serializers.CharField(max_length = 10)
    