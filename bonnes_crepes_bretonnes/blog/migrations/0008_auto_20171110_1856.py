# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-10 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_sarrasin_sucree'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sarrasin',
        ),
        migrations.DeleteModel(
            name='Sucree',
        ),
    ]
