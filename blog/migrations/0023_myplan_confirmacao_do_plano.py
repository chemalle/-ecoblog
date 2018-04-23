# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180311_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='myplan',
            name='confirmacao_do_plano',
            field=models.CharField(choices=[('STARTUP', 'startup'), ('Business', 'business'), ('Corporate', 'Corporate')], default='startup', max_length=10),
            preserve_default=False,
        ),
    ]
