# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20170217_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercourse',
            old_name='name',
            new_name='user',
        ),
    ]
