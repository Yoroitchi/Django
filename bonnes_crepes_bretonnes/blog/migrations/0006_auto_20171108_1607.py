# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171108_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='contenu',
        ),
        migrations.AddField(
            model_name='article',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='preparation',
            field=models.TextField(null=True),
        ),
    ]