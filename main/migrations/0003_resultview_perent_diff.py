# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_resultview'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultview',
            name='perent_diff',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True),
        ),
    ]
