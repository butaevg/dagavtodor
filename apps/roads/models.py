#coding: utf-8
from django.db import models
from users.models import DUser


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



TYPE_OF_OBJ = (
    ('str', 'Строительство'),
    ('rec', 'Реконструкция'),
    ('rem', 'Ремонт'),
)

class Road(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    body = models.TextField(blank=True, verbose_name='Описание')
    pic = models.ImageField(max_length=250, blank=True, upload_to='roads', verbose_name='Карта-схема')
    cat = models.CharField(max_length=3, choices=TYPE_OF_OBJ, verbose_name='Вид')
    contractor = models.ForeignKey(DUser, blank=True, verbose_name='Подрядчик')
    onsite = models.BooleanField(default=False, verbose_name='Показывать на сайте')
    report = models.BooleanField(default=False, verbose_name='Есть отчеты')
    complete = models.BooleanField(default=False, verbose_name='Завершен')
  
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'Объекты'

class Report(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    road = models.ForeignKey(Road, related_name='reps', verbose_name='Объект')

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return '/roads/progress/reports/%s/' % self.road_id

class ReportImg(models.Model):
    url = models.ImageField(max_length=250, upload_to='roads/%Y-%m-%d/', verbose_name='Фото')
    report = models.ForeignKey(Report, related_name='pics', verbose_name='Отчет')

    def get_absolute_url(self):
        return '/roads/progress/upload_img/%s/' % self.report_id


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