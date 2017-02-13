# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_post_tweet_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='markup',
            field=models.CharField(blank=True, choices=[('markdown', 'Markdown')], max_length=25, verbose_name='Markup'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=90, verbose_name='Slug'),
        ),
    ]
