# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-18 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_ecd01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecd01',
            name='UF',
            field=models.CharField(help_text='Qual a sua UF', max_length=2),
        ),
    ]
