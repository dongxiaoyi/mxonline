# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[(b'cj', b'\xe5\x88\x9d\xe7\xba\xa7'), (b'zj', b'\xe4\xb8\xad\xe7\xba\xa7'), (b'gj', b'\xe9\xab\x98\xe7\xba\xa7')], max_length=2, verbose_name='\u96be\u5ea6'),
        ),
    ]