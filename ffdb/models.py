from django.db import models

# Create your models here.
class Asset(models.Model):
    type = models.CharField(max_length=10)
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=10)
    currency = models.CharField(max_length=5)