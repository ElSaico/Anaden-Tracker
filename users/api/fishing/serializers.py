from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Fish, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class FishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fish
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
