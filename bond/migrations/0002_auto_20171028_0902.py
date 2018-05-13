# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='name',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bond',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
