# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20170217_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercourse',
            old_name='user',
            new_name='name',
        ),
    ]
