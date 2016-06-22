#coding: utf-8
from django.db import models

class Map(models.Model):
    rayon = models.CharField(max_length=100, verbose_name='Район')
    plos = models.CharField(max_length=20, verbose_name='Площадь')
    nal_dor_obs = models.CharField(max_length=20, verbose_name='Наличие дорог на тыс. км.')
    selo = models.CharField(max_length=20, verbose_name='Наличие сел')
    selo_bezd = models.CharField(max_length=20, verbose_name='в т.ч. с бездор. покрытием')
    prot_obs = models.CharField(max_length=20, verbose_name='Протяженность дорог')
    res_dor = models.CharField(max_length=20, verbose_name='Республиканские')
    mest_dor = models.CharField(max_length=20, verbose_name='Местные')
    res_dor_asf = models.CharField(max_length=20, verbose_name='Республиканские - асфальт')
    mest_dor_asf = models.CharField(max_length=20, verbose_name='Местные - асфальт')
    map_rayon = models.ImageField(max_length=100, blank=True, upload_to='maps', verbose_name='Карта')
    
    def __unicode__(self):
        return self.rayon
        
    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'Карты районов'