# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-28 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20171106_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfomation',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone'),
        ),
    ]
