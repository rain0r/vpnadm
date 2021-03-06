# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-12-17 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpnadm', '0008_auto_20181217_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='serversettings',
            name='server_ipv4',
            field=models.GenericIPAddressField(default='10.0.0.1', protocol='IPv4', verbose_name='Server IPv4 Address'),
        ),
        migrations.AddField(
            model_name='serversettings',
            name='server_ipv6',
            field=models.GenericIPAddressField(default='fd00:db8::1', protocol='IPv6', verbose_name='Server IPv6 Address'),
        ),
        migrations.AlterField(
            model_name='serversettings',
            name='first_ipv6',
            field=models.GenericIPAddressField(default='fd00:db8::2', protocol='IPv6', verbose_name='First Client IPv6 Address'),
        ),
    ]
