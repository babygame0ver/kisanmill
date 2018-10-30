# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customercorner', '0017_auto_20171028_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertCorner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Description', models.CharField(max_length=1500)),
                ('Technique_name', models.CharField(max_length=150)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customercorner.Product')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
