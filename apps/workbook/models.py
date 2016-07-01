#coding: utf-8
from django.db import models
from users.models import DUser 
from datetime import datetime


class Road(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    dep = models.ForeignKey(DUser, blank=True, verbose_name='ДЭП')
  
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'дорогу'
        verbose_name_plural = 'Дороги'


class Workbook(models.Model):
    dep = models.ForeignKey(DUser, related_name="dep_name", verbose_name='ДЭП')
    road = models.ForeignKey(Road, related_name="road_name", verbose_name='Дорога')
    file = models.FileField(max_length=250, upload_to='workbook/%Y-%m-%d/', verbose_name='Файл')
    putdate = models.DateField(default=datetime.now, verbose_name='Дата')
    
    class Meta:
        ordering = ['-putdate',]


