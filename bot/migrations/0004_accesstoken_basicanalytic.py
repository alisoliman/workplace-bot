# Generated by Django 2.0 on 2018-03-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20180309_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Access Token',
                'verbose_name_plural': 'Access Token',
            },
        ),
        migrations.CreateModel(
            name='BasicAnalytic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogv_approved', models.IntegerField(default=0)),
                ('igv_approved', models.IntegerField(default=0)),
                ('ogt_approved', models.IntegerField(default=0)),
                ('igt_approved', models.IntegerField(default=0)),
                ('oge_approved', models.IntegerField(default=0)),
                ('ige_approved', models.IntegerField(default=0)),
                ('ogv_realized', models.IntegerField(default=0)),
                ('igv_realized', models.IntegerField(default=0)),
                ('ogt_realized', models.IntegerField(default=0)),
                ('igt_realized', models.IntegerField(default=0)),
                ('oge_realized', models.IntegerField(default=0)),
                ('ige_realized', models.IntegerField(default=0)),
                ('ogv_completed', models.IntegerField(default=0)),
                ('igv_completed', models.IntegerField(default=0)),
                ('ogt_completed', models.IntegerField(default=0)),
                ('igt_completed', models.IntegerField(default=0)),
                ('oge_completed', models.IntegerField(default=0)),
                ('ige_completed', models.IntegerField(default=0)),
                ('total_approved', models.IntegerField(default=0)),
                ('total_realized', models.IntegerField(default=0)),
                ('total_completed', models.IntegerField(default=0)),
            ],
        ),
    ]
