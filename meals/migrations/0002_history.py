# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_type', models.CharField(max_length=200)),
                ('event_count', models.IntegerField(default=0)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal')),
            ],
        ),
    ]