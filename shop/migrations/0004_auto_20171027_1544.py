# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20171027_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='Prize',
            new_name='Price',
        ),
        migrations.AlterField(
            model_name='auction',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
