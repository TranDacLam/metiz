# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171002_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('key_query', models.CharField(max_length=255, unique=True)),
                ('is_draft', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
