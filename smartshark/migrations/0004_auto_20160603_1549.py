# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0003_auto_20160603_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mongorole',
            name='users',
        ),
        migrations.AddField(
            model_name='smartsharkuser',
            name='roles',
            field=models.ManyToManyField(to='smartshark.MongoRole'),
        ),
    ]
