# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0011_meal_last_suggested_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='last_selected_date',
            field=models.DateTimeField(null=True),
        ),
    ]
