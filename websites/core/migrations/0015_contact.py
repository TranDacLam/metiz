# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-10 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20171024_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]