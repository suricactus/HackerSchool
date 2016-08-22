# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-18 07:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20160818_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 7, 20, 3, 300847, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 7, 20, 3, 300911, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 7, 20, 3, 320905, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 7, 20, 3, 320961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_logo',
            field=models.FileField(upload_to=b''),
        ),
    ]