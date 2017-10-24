# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_movie_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_api_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Movie API ID'),
        ),
    ]
