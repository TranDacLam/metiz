# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20171116_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='newoffer',
            name='end_date',
            field=models.DateField(default=None, verbose_name='End Date'),
        ),
    ]