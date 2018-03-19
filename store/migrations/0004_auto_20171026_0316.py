# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-25 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cartbill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Cart')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='cart',
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ManyToManyField(through='store.Sale', to='store.Cart')
        ),
        migrations.AddField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Item'),
        ),
    ]
