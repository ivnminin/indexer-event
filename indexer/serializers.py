from django.contrib.auth.models import User
from rest_framework import serializers

from . models import EventBought


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class EventBoughSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventBought
        fields = ['buyer_address', 'amount', 'tx']
