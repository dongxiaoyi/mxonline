# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-15 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0, verbose_name='\u5e74\u9f84'),
        ),
    ]