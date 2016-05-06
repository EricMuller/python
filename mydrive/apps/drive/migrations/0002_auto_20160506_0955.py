# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=512)),
                ('contentType', models.CharField(max_length=30)),
                ('version', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DriveNode',
            new_name='Repository',
        ),
        migrations.RemoveField(
            model_name='document',
            name='folder',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='file',
            name='repository',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.Repository', verbose_name='Repository'),
        ),
    ]