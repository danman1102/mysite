# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='Date Added')),
                ('counter', models.IntegerField(default=0)),
                ('last_selected_date', models.DateTimeField(verbose_name='Last Occurrence')),
                ('category_text', models.CharField(max_length=200)),
            ],
        ),
    ]
