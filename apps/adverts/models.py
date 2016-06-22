#coding: utf-8
from django.db import models 

class Advert(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    putdate = models.DateField(verbose_name='Дата')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-putdate']
