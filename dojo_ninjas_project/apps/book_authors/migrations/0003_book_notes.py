# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.TextField(default='Please create some notes for each book.'),
            preserve_default=False,
        ),
    ]
