# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20171027_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='auction',
            name='image',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
