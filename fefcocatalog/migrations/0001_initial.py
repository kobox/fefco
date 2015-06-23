# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FefcoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(default=b'', max_length=254, verbose_name=b'Tytu\xc5\x82')),
                ('description', models.TextField(null=True, verbose_name=b'Opis', blank=True)),
                ('picture', models.ImageField(default=b'fefco_pics/default.png', upload_to=b'fefco_pics/', verbose_name=b'Kategoria FEFCO')),
                ('fefcocode', models.CharField(max_length=5)),
                ('parent_category', models.ForeignKey(blank=True, to='fefcocatalog.FefcoCategory', null=True)),
            ],
        ),
    ]
