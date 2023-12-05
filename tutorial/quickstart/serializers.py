"""Serializers of quickstart"""

from django.contrib.auth.models import Group, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of User"""
    class Meta:
        """Meta class"""
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of Group"""
    class Meta:
        """Meta class"""
        model = Group
        fields = ['url', 'name']