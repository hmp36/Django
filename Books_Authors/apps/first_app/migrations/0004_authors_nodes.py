# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20171220_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='nodes',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
