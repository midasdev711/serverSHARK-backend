# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0022_auto_20160616_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mongo_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]