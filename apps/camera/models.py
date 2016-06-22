#coding: utf-8
from django.db import models

class Cam3g(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    folder = models.CharField(max_length=100, verbose_name='Каталог')
    ip = models.CharField(max_length=50, blank=True, verbose_name='IP-адрес')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = '3g-камеру'
        verbose_name_plural = '3g-камеры'


class CamIp(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    html = models.TextField(verbose_name='HTML-код')
    img = models.ImageField(upload_to='webcam', verbose_name='Картинка')
    ip = models.CharField(max_length=50, blank=True, verbose_name='IP-адрес')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'ip-камеру'
        verbose_name_plural = 'ip-камеры'