# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-12-17 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpnadm', '0009_auto_20181217_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='bytes_received',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='bytes_sent',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='client_os',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='client',
            name='connected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='connected_duration',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='last_connection_change',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='last_remote_ip',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]