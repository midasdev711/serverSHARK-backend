# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0020_pluginexecution_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='pluginexecution',
            name='error_log',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pluginexecution',
            name='output_log',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
