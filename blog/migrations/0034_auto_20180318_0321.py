# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-18 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20180318_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecd01',
            name='CLOSING',
        ),
        migrations.RemoveField(
            model_name='ecd01',
            name='INITIAL',
        ),
    ]
