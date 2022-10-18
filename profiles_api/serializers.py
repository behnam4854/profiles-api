# from dataclasses import fields
# import email
# from pyexpat import model
from rest_framework import serializers

from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serialzers for a user profile"""
    class Meta:
        model = models.UserProfile
        fields = ('id' , 'email' , 'name' ,'password')
        extra_kwargs ={
            'password' : {
                'write_only' :True,
                'style' : {'input_type' : 'password'}
            }
        }
    
    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email =validated_data['email'],
            name= validated_data['name'],
            password = validated_data['password']
        )

        return user