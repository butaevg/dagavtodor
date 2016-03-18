#coding: utf-8
from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name='Раздел')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'Раздел'


class Page(models.Model):
    title = models.CharField(max_length=512, verbose_name='Заголовок')
    slug = models.SlugField(max_length=512, verbose_name='URL')
    body = models.TextField(verbose_name='Текст')
    section = models.ForeignKey(Section, related_name="sec")
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = 'страницу'
        verbose_name_plural = 'Страницы'