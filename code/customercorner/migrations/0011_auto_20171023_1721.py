# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0010_auto_20171023_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrionalcontent',
            name='Carbohydrates',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrionalcontent',
            name='Protein',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrionalcontent',
            name='Sugar',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
