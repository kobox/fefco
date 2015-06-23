# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class FefcoCategory(models.Model):

    slug = models.SlugField(max_length=50)
    title = models.CharField('Tytuł', default='', max_length=254, blank=False, null=False)
    description = models.TextField('Opis', blank=True, null=True)
    picture = models.ImageField('Kategoria FEFCO', default='fefco_pics/default.png', upload_to='fefco_pics/',
                                blank=False, null=False)
    fefcocode = models.CharField(max_length=5)
    parent_category = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.title

#subcategories = Category.objects.filter(parent_category__id=target_category.id)