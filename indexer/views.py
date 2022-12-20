from django.contrib.auth.models import User
from rest_framework import viewsets

from . import serializers
from . import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class EventBoughtViewSet(viewsets.ModelViewSet):
    queryset = models.EventBought.objects.all()
    serializer_class = serializers.EventBoughSerializer
