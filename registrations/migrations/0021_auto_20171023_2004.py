# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-23 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0020_participant_ems_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regsoft.Bill'),
        ),
    ]
