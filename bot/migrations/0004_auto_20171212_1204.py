# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-12 12:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_survey_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 12, 12, 4, 40, 649209)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 12, 12, 4, 40, 649244)),
        ),
    ]