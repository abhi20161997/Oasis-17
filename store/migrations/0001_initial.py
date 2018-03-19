# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-25 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0022_auto_20171024_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.CharField(max_length=20)),
                ('is_bitsian', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(default=0)),
                ('front_pic', models.ImageField(null=True, upload_to='store/front_pics/')),
                ('back_pic', models.ImageField(null=True, upload_to='store/back_pics/')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Cart')),
                ('colour', models.ManyToManyField(blank=True, null=True, to='store.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='store.Size'),
        ),
    ]
