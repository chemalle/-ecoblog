# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-17 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0056_auto_20180411_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='holerite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo do colaborador', max_length=100)),
                ('salario', models.FloatField()),
                ('descanso', models.FloatField()),
                ('comissoes', models.FloatField()),
                ('salario_familia', models.FloatField()),
                ('adic_sal_familia', models.FloatField()),
                ('horas_extras_55', models.FloatField()),
                ('vale_transporte', models.FloatField()),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='Estado_Civil',
            field=models.CharField(choices=[('Casado', 'Casado'), ('Solteiro', 'Solteiro'), ('Divorciado', 'Divorciado'), ('Desquitado', 'Desquitado'), ('Viúvo', 'Viúvo')], help_text='Estado Civil colaborador', max_length=30),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Forma_Pagamento',
            field=models.CharField(choices=[('MENSAL', 'MENSAL'), ('QUINZENAL', 'QUINZENAL'), ('SEMANAL', 'SEMANAL')], max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Grau_Instrucao',
            field=models.CharField(choices=[('Analfabeto', 'Analfabeto'), ('Ensino Fundamental Incompleto', 'Ensino Fundamental Incompleto'), ('Ensino Fundamental Completo', 'Ensino Fundamental Completo'), ('Ensino Médio Incompleto', 'Ensino Médio Incompleto'), ('Ensino Médio Completo', 'Ensino Médio Completo'), ('Superior completo (ou Graduação)', 'Superior completo (ou Graduação)'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('PHD', 'PHD')], help_text='Escolaridade do colaborador', max_length=30),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Tipo_Salario',
            field=models.CharField(choices=[('MENSALISTA', 'MENSALISTA'), ('HORISTA', 'HORISTA')], max_length=50),
        ),
    ]
