from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=16)
    last_price = models.DecimalField(decimal_places=6, max_digits=15)


class Portfolio(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=16)
    client_code = models.CharField(max_length=16)
    total = models.PositiveIntegerField()
    acquisition_price = models.DecimalField(decimal_places=6, max_digits=15)


class ResultView(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=256)
    buy_price = models.DecimalField(decimal_places=6, max_digits=15, default=0)
    last_sell_price = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    amount = models.PositiveIntegerField()
    target = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    cur_price = models.DecimalField(decimal_places=6, max_digits=15)
    percent_diff = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)