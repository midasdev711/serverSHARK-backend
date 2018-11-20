# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-11-20 23:06
from __future__ import unicode_literals

from django.db import migrations
from smartshark.models import Plugin

def setAllSemVerTo2(apps, schema_editor):

    for plugins in Plugin.objects.all():
        plugins.version = '2.0.0'
        plugins.save()


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0037_auto_20181120_2356'),
    ]

    operations = [
        migrations.RunPython(setAllSemVerTo2),
    ]
