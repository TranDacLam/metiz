# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_movie_movie_api_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_api_id',
            field=models.CharField(default='00000000', max_length=100, verbose_name='Movie API ID'),
        ),
    ]