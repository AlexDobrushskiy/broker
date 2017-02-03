from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    amount = models.PositiveIntegerField(null=True, blank=True)
    target = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    cur_price = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    percent_diff = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    has_dividends = models.BooleanField(default=False)
    year_amount = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)
    divident_year_percent = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)


@receiver(post_save, sender=ResultView, dispatch_uid="result_view_post_save")
def result_view_post_save(sender, instance, created, **kwargs):
    comment, created = Comment.objects.get_or_create(code=instance.code)
    comment.comment = instance.comment
    comment.save()

    dividend, created = Dividend.objects.get_or_create(code=instance.code)
    dividend.has_dividends = instance.has_dividends
    dividend.year_amount = instance.year_amount
    dividend.save()


class Comment(models.Model):
    code = models.CharField(max_length=16, unique=True)
    comment = models.TextField(null=True, blank=True)


class Dividend(models.Model):
    code = models.CharField(max_length=16, unique=True)
    has_dividends = models.BooleanField(default=False)
    year_amount = models.DecimalField(decimal_places=6, max_digits=15, null=True, blank=True)