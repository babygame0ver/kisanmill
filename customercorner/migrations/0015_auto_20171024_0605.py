# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0014_auto_20171024_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_type',
            old_name='categories',
            new_name='name',
        ),
    ]
