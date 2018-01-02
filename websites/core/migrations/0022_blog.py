# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-28 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20171213_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('image', models.ImageField(max_length=1000, upload_to='blogs', verbose_name='Image')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_draft', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]