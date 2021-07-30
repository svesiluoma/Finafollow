from django.db import models
from django.db.models.fields import CharField


class AssetType(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"



class Asset(models.Model):
    asset_type = models.ForeignKey('AssetType', on_delete=models.PROTECT)
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=10)
    currency = models.CharField(max_length=5) 

    def __str__(self) -> str:
        return f"{self.asset_type}: {self.ticker} {self.name}, country: {self.country}, currency: {self.currency}"

    def get_ticker(self) -> str:
        return self.ticker

    def get_asset_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.get_ticker()} {self.get_asset_name()}, buy date: {self.buy_date()}, amount: {self.amount}, left: {self.culeft}"


class BuySlot(models.Model):
   asset = models.ForeignKey('Asset', on_delete=models.PROTECT)
   amount = models.BigIntegerField
   left = models.BigIntegerField
   buy_date = models.DateField() 
   buy_price = models.FloatField()
   buy_cost = models.FloatField()
   buy_price_pc = models.FloatField()

   def __str__(self) -> str:
       return f"{self.get_ticker()} {self.get_asset_name()}, buy date: {self.buy_date()}, amount: {self.amount}, left: {self.culeft}"

class SellSlot(models.Model):
   asset = models.ForeignKey('Asset', on_delete=models.PROTECT)
   amount = models.BigIntegerField
   sell_date = models.DateField() 
   sell_price = models.FloatField()
   sell_cost = models.FloatField()
   sell_price_pc = models.FloatField()

   def __str__(self) -> str:
        return f"{self.get_ticker()} {self.get_asset_name()}, buy date: {self.buy_date()}, amount: {self.amount}, left: {self.culeft}"


class Dividend(models.Model):
   asset = models.ForeignKey('Asset', on_delete=models.PROTECT)
   dividend_date = models.DateField()
   dividend_price = models.FloatField()