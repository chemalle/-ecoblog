# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20180311_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='myplan',
            name='tamanho',
            field=models.CharField(choices=[('media', 'media'), ('pequena', 'pequena')], default='pequena', max_length=10),
            preserve_default=False,
        ),
    ]
