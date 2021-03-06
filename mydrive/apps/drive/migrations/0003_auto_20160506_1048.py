# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_auto_20160506_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=30)),
                ('libelle', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='repository',
            name='name',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.TypeRepository', verbose_name='TypeRepository'),
        ),
    ]
