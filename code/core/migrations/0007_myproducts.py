# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0015_auto_20171024_0605'),
        ('core', '0006_auto_20171027_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_list', models.ManyToManyField(to='customercorner.Product')),
            ],
        ),
    ]
