#coding: utf-8  
from django.db import models 
from datetime import datetime

class Article(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    pic = models.ImageField(max_length=250, blank=True, upload_to='articles/%Y-%m-%d/', verbose_name='Фото')
    putdate = models.DateField(verbose_name='Дата', default=datetime.now)
    source = models.CharField(max_length=512, blank=True, verbose_name='Ссылка на источник')
    source_name = models.CharField(max_length=100, blank=True, verbose_name='Источник')

    class Meta:
        ordering = ["-putdate"]
    