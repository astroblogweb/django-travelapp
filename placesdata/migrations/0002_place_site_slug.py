# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placesdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='site_slug',
            field=models.CharField(default='default_slug', max_length=100, verbose_name='site_state'),
            preserve_default=False,
        ),
    ]
