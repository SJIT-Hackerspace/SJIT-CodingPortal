# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-11 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0017_auto_20160911_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('TestCases', models.CharField(max_length=200, verbose_name='Test Cases')),
                ('Output', models.CharField(max_length=200)),
                ('subCategory', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=200, verbose_name='Option1')),
                ('op2', models.CharField(max_length=200, verbose_name='Option2')),
                ('op3', models.CharField(max_length=200, verbose_name='Option3')),
                ('op4', models.CharField(max_length=200, verbose_name='Option4')),
                ('Answer', models.CharField(max_length=200)),
                ('subCategory', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Verbal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=200, verbose_name='Option1')),
                ('op2', models.CharField(max_length=200, verbose_name='Option2')),
                ('op3', models.CharField(max_length=200, verbose_name='Option3')),
                ('op4', models.CharField(max_length=200, verbose_name='Option4')),
                ('Answer', models.CharField(max_length=200)),
                ('subCategory', models.CharField(max_length=200)),
            ],
        ),
    ]
