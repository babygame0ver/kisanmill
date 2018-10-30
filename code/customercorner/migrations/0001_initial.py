# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=15)),
                ('Product_type', models.CharField(choices=[(b'DAIRY', b'Dairy Product'), (b'FRUIT', b'Fruits'), (b'VEGETABLES', b'Vegetables')], max_length=15)),
                ('Product_version', models.CharField(max_length=15)),
            ],
        ),
    ]
