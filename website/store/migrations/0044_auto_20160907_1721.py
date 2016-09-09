# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-07 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_auto_20160907_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='made_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
