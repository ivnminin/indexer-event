from django.db import models


class Contract(models.Model):
    class ContractType(models.IntegerChoices):
        TOKEN = 1
        TOKEN_SALE = 2
    contract_type = models.IntegerField(choices=ContractType.choices)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=42)
