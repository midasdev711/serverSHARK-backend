# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0023_project_mongo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='description',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
    ]
