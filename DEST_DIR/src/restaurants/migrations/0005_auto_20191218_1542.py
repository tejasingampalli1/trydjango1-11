# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-12-18 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantlocation_timestmap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='timestmap',
            new_name='timestamp',
        ),
    ]