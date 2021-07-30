from django.contrib import admin

from .models import AssetType, Asset, BuySlot, SellSlot, Dividend

admin.site.register(AssetType)
admin.site.register(Asset)
admin.site.register(BuySlot)
admin.site.register(SellSlot)
admin.site.register(Dividend)
