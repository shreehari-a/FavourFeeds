# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0010_auto_20170617_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_feedwebsite',
            old_name='userid',
            new_name='user_id',
        ),
    ]