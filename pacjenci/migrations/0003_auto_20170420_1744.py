# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacjenci', '0002_auto_20170420_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patients',
            new_name='Patient',
        ),
    ]
