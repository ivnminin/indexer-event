from django.contrib import admin

from . import models


class EventBoughtAdmin(admin.ModelAdmin):
    list_display = ('buyer_address', 'amount', 'tx')

    class Meta:
        model = models.EventBought


admin.site.register(models.EventBought, EventBoughtAdmin)
