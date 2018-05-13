# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 09:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auction_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
