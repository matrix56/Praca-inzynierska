# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('pesel', models.IntegerField(max_length=11)),
            ],
        ),
    ]
