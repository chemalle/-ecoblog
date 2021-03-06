# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-20 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_igpm_selic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset', models.CharField(help_text='Qual o ativo voce quer analisar?', max_length=10)),
                ('Nome_da_Empresa', models.CharField(help_text='Qual o nome da sua empresa?', max_length=200)),
                ('email', models.EmailField(help_text='Qual o seu e-mail?', max_length=200)),
                ('Seu_nome', models.CharField(help_text='Qual o seu nome?', max_length=200)),
                ('Seu_cargo', models.CharField(help_text='Qual o seu cargo?', max_length=200)),
                ('Segmento', models.CharField(choices=[('SERVIÇOS', 'SERVIÇOS'), ('INDUSTRIA', 'INDUSTRIA'), ('COMÉRCIO', 'COMÉRCIO'), ('AGRONEGÓCIO', 'AGRONEGÓCIO'), ('STARTUP', 'STARTUP')], help_text='Insira seu segmento', max_length=12)),
                ('Dicas', models.CharField(help_text='Gostaria de receber dicas de Investimento?', max_length=12)),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
