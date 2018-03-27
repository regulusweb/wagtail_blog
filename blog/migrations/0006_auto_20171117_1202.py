# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151019_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_pages', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='body'),
        ),
    ]
