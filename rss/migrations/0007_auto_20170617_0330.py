# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0006_auto_20170616_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeddetail',
            name='feed_id',
        ),
        migrations.AddField(
            model_name='feeddetail',
            name='feed_id',
            field=models.ManyToManyField(to='rss.FeedWebsite'),
        ),
    ]
