# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170509_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=2000, verbose_name='设备名称'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=5000, verbose_name='产品名称'),
        ),
    ]
