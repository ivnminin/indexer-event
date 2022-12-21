from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN

from . import models
from . import serializers


class EventBoughtTests(TestCase):

    buyer_address = '0x123'
    amount = '100'
    tx = '0xff00'

    def setUp(self):
        models.EventBought.objects.create(
            pk=1,
            buyer_address=self.buyer_address,
            amount=self.amount,
            tx=self.tx,
        )

    def test_model(self):
        event_bought = models.EventBought.objects.get(pk=1)
        self.assertEqual(event_bought.buyer_address, self.buyer_address)
        self.assertEqual(event_bought.amount, self.amount)
        self.assertEqual(event_bought.tx, self.tx)


class EventBoughtTestsView(APITestCase):

    buyer_address = '0x123'
    amount = '100'
    tx = '0xff00'

    def setUp(self):
        self.event_bought = models.EventBought.objects.create(
            pk=1,
            buyer_address=self.buyer_address,
            amount=self.amount,
            tx=self.tx,
        )

    def test_view(self):
        response = self.client.get('/api/event-bought/')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_view_get_item(self):
        response = self.client.get('/api/event-bought/1/')
        serializer = serializers.EventBoughSerializer(self.event_bought)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_view_get_does_not_exist_item(self):
        response = self.client.get('/api/event-bought/123/')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_view_unsupported_method_post(self):
        response = self.client.post('/api/event-bought/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_put(self):
        response = self.client.put('/api/event-bought/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_patch(self):
        response = self.client.post('/api/event-bought/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_delete(self):
        response = self.client.delete('/api/event-bought/1/')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
