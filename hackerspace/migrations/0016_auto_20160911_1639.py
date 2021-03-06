# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-11 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0015_batches_programming_subcategories_programmingquestion_quiz_quiz_subcategories_students_test_user_ver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmingquestion',
            name='subCategory',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='subCategory',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='test',
            name='Batch',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='ProgrammingTagName',
            field=models.IntegerField(verbose_name='Programming Tags'),
        ),
        migrations.AlterField(
            model_name='test',
            name='QuizTagName',
            field=models.IntegerField(verbose_name='Quiz Tags'),
        ),
        migrations.AlterField(
            model_name='verbal',
            name='subCategory',
            field=models.CharField(max_length=200),
        ),
    ]
