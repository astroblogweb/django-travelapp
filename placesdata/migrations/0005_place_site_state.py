# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placesdata', '0004_auto_20170926_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='site_state',
            field=models.CharField(default='default state', max_length=50, verbose_name='site_state'),
            preserve_default=False,
        ),
    ]
