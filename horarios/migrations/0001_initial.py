# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('salida', models.DateTimeField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
