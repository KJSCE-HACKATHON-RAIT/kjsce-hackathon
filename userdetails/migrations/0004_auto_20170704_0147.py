# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0003_auto_20170704_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size_chart',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]