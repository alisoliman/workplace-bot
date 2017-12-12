# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-12 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20171212_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[(1, 'Message'), (2, 'Postback')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 12, 12, 6, 8, 777615)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 12, 12, 6, 8, 777582)),
        ),
    ]
