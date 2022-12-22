from django.db import models
from django.core.exceptions import ValidationError


class Contract(models.Model):
    class ContractType(models.IntegerChoices):
        TOKEN = 1
        TOKEN_SALE = 2
    contract_type = models.IntegerField(choices=ContractType.choices)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.name

class EventBought(models.Model):
    buyer_address = models.CharField(max_length=42, verbose_name='address')
    amount = models.CharField(max_length=255)
    tx = models.CharField(max_length=255)

    class Meta:
        ordering = ['buyer_address']


class EventTransfer(models.Model):
    _from = models.CharField(max_length=42, verbose_name='from')
    to = models.CharField(max_length=42)
    amount = models.CharField(max_length=255)
    tx = models.CharField(max_length=255)


class Event(models.Model):
    class EventType(models.IntegerChoices):
        BOUGHT = 1
        TRANSFER = 2
    event_type = models.IntegerField(choices=EventType.choices)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="events")

    def save(self, *args, **kwargs):
        if Event.objects.filter(contract__address=self.contract.address, event_type=self.event_type).exists():
            raise ValidationError('Event exists')
        super().save(*args, **kwargs)

    @property
    def event(self):
        if self.event_type == self.EventType.BOUGHT:
            return EventBought
        elif self.event_type == self.EventType.TRANSFER:
            return EventTransfer
