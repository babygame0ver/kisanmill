# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customercorner', '0015_auto_20171024_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_all_products', models.ManyToManyField(related_name='Myproducts', to='customercorner.Product')),
            ],
        ),
    ]