# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0018_auto_20171021_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='registrations.Participant'),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader_bitsian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bitsian_leader', to='ems.Bitsian'),
        ),
    ]
