from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from functools import wraps
import jwt

from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer

from manejadorOrdenes.serializers import UserSerializer, GroupSerializer


def home(request):
    return HttpResponse("Hello World")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]