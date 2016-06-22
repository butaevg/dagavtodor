#coding: utf-8
from django.db import models
from users.models import DUser

class Psd(models.Model):
    name = models.CharField(max_length=512, verbose_name='Объект')
    price = models.FloatField(verbose_name='Стоимость')
    contractor = models.ForeignKey(DUser, related_name='proj', verbose_name='Проектировщик')
    exe = models.FloatField(blank=True, verbose_name='Выполнение')
    exe_perc = models.IntegerField(blank=True, default=0, verbose_name='Выполнение, %')
    getsum = models.FloatField(blank=True, verbose_name='Получено')
    exe_getsum = models.IntegerField(blank=True, default=0, verbose_name='Получено, %')
  
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'ПСД'
        verbose_name_plural = 'ПСД'
        ordering = ['name', ]