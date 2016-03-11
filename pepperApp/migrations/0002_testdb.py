# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldChar', models.CharField(max_length=30)),
                ('fieldInt', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]