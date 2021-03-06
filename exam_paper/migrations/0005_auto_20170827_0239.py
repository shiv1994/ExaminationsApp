# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 02:39
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_paper', '0004_auto_20170827_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampaper',
            name='examPaperAnswers',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='examPaperQuestion',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='examPaperReport',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to=b''),
        ),
    ]
