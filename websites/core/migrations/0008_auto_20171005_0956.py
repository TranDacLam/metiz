# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171003_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
