from django.test import TestCase

from . import models


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
