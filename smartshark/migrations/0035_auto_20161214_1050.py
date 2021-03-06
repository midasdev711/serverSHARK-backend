# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-14 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0034_auto_20161201_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='pluginexecution',
            name='execution_type',
            field=models.CharField(blank=True, choices=[('all', 'Executed on all revisions'), ('new', 'Executed on new revisions'), ('rev', 'Executed on specified revisions'), ('error', 'Executed on revisions that previously threw an error')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='pluginexecution',
            name='repository_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pluginexecution',
            name='revisions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
