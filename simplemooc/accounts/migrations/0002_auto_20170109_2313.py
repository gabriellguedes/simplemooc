# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 23:13
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
            ],
            options={
                'verbose_name_plural': 'Novas Senhas',
                'verbose_name': 'Nova Senha',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário'),
        ),
        migrations.AddField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
