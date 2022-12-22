from django.contrib import admin

from . import models


class EventBoughtAdmin(admin.ModelAdmin):
    list_display = ('buyer_address', 'amount', 'tx')
    search_fields = ('buyer_address', 'tx')

    class Meta:
        model = models.EventBought


class EventTransferAdmin(admin.ModelAdmin):
    list_display = ('_from', 'to', 'amount', 'tx')
    search_fields = ('_from', 'to', 'tx')

    class Meta:
        model = models.EventTransfer


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'contract')

    class Meta:
        model = models.Event


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_type', 'name', 'address')

    class Meta:
        model = models.Contract


admin.site.register(models.EventBought, EventBoughtAdmin)
admin.site.register(models.EventTransfer, EventTransferAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Contract, ContractAdmin)
