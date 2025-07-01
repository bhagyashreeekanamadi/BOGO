from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User 
        fields=('username','email','password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
