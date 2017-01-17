# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reestr', '0003_auto_20161213_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genre',
            new_name='date_of_birht',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_logo',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_title',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='address',
            field=models.CharField(default='', max_length=250, verbose_name='Адреса проживання'),
        ),
        migrations.AddField(
            model_name='album',
            name='date_of_entry',
            field=models.CharField(default='', max_length=250, verbose_name='Дата реєстрації'),
        ),
        migrations.AddField(
            model_name='album',
            name='middle_name',
            field=models.CharField(default='', max_length=250, verbose_name='Ім’я'),
        ),
        migrations.AlterField(
            model_name='album',
            name='first_name',
            field=models.CharField(default='', max_length=250, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='album',
            name='place_of_birth',
            field=models.CharField(default='', max_length=250, verbose_name='Місце народження'),
        ),
    ]