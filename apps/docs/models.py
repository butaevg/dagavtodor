#coding: utf-8
from django.db import models

class DocsCat(models.Model):
    name = models.CharField(max_length=300, verbose_name='Категория')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории документов'


class Doc(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    url = models.FileField(max_length=250, upload_to='docs', verbose_name='Файл')
    cat = models.ForeignKey(DocsCat, related_name="cat", verbose_name='Категория')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'Документы'