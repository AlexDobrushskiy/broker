# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170131_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultview',
            name='cur_price',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True),
        ),
    ]
