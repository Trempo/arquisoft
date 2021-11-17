from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']