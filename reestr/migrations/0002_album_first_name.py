# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reestr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='first_name',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]
