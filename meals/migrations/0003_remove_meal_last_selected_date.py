# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='last_selected_date',
        ),
    ]
