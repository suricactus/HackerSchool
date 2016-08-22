# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-18 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20160818_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='asd', max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='asd', max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 8, 34, 23, 603708, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 8, 34, 23, 603761, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 8, 34, 23, 613676, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 8, 34, 23, 613728, tzinfo=utc), editable=False),
        ),
    ]