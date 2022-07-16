from pyexpat import model
from unicodedata import name
from rest_framework import serializers
from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """ Serializers for api """
    
    name = serializers.CharField(max_length = 10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {
                    'input_type' : 'password'
                }
            }
        }
    
    
    def create(self, validated_data):
        user = models.UserProfile.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
  
  
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwarg = {'user_profile' : {'read_only' : True}}
        