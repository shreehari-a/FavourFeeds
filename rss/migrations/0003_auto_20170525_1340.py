# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-25 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0002_auto_20170524_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.TimeField()),
                ('updated_time', models.TimeField(auto_now=True)),
                ('title', models.TextField()),
                ('feed', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
