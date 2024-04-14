# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Description',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
