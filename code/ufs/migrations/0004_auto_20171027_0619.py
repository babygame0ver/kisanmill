# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufs', '0003_remove_message_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Images',
            field=models.FileField(upload_to=b''),
        ),
    ]
