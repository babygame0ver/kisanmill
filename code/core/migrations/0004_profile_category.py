# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171026_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(choices=[('Farmer', 'Farmer'), ('Firm', 'Firm')], default=0, max_length=15),
            preserve_default=False,
        ),
    ]
