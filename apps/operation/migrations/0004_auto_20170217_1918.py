# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20170217_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercourse',
            old_name='user_name',
            new_name='user',
        ),
    ]
