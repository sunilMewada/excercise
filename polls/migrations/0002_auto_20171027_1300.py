# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excercise',
            name='accept',
        ),
        migrations.RemoveField(
            model_name='excercise',
            name='reject',
        ),
    ]