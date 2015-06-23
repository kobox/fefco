# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fefcocatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fefcocategory',
            name='parent_category',
            field=models.ForeignKey(related_name='subcategories', blank=True, to='fefcocatalog.FefcoCategory', null=True),
        ),
    ]
