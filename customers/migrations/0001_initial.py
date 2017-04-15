# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('street_1', models.CharField(max_length=255)),
                ('street_2', models.CharField(blank=True, default='', max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postal_code', models.CharField(max_length=20)),
            ],
        ),
    ]