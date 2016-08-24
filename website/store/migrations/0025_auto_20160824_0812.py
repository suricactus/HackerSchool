# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-24 08:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20160819_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': (('view_task', 'View task'),), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 24, 8, 12, 36, 892441, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 8, 12, 36, 892514, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 24, 8, 12, 36, 893895, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 8, 12, 36, 893961, tzinfo=utc), editable=False),
        ),
    ]
