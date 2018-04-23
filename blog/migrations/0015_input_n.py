# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_delete_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='n',
            field=models.CharField(default=django.utils.timezone.now, help_text='10 characters max.', max_length=10),
            preserve_default=False,
        ),
    ]