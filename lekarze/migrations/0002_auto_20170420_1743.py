# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lekarze', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]
