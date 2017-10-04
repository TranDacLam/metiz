# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-03 06:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('image', models.ImageField(max_length=255, upload_to='slide_home')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('is_draft', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='movietype',
            name='description',
        ),
        migrations.AlterField(
            model_name='movie',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movietype',
            name='name',
            field=models.CharField(choices=[('', '----'), ('2d', '2D'), ('3d', '3D'), ('4dx', '4DX'), ('imax', 'IMAX'), ('screenx', 'SCREEN X')], max_length=50),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='apply_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 3, 6, 53, 30, 139330)),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='apply_for',
            field=models.CharField(choices=[('all', 'ALL'), ('member', 'Member')], default='all', max_length=50),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='condition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='movies',
            field=models.ManyToManyField(blank=True, null=True, to='core.Movie'),
        ),
        migrations.AlterField(
            model_name='newoffer',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
