# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20171028_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='images',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
