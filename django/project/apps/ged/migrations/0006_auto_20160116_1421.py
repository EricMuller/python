# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ged', '0005_auto_20160116_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
