from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework import filters
from rest_framework import viewsets

from . import serializers
from . import models


class EventBoughtFilter(FilterSet):
    min_price = NumberFilter(field_name='amount', lookup_expr='gte')
    max_price = NumberFilter(field_name='amount', lookup_expr='lte')

    class Meta:
        model = models.EventBought
        fields = ['amount']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class EventBoughtViewSet(viewsets.ModelViewSet):
    queryset = models.EventBought.objects.all().order_by('-amount')
    serializer_class = serializers.EventBoughSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EventBoughtFilter
    ordering_fields = ['amount']
