# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=32, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=32, verbose_name='Longitude')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('latitude', 'longitude')]),
        ),
    ]
