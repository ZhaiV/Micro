# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160328_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
