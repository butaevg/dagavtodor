#coding: utf-8
from django.db import models
from users.models import DUser


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
    contractor = models.ForeignKey(DUser, related_name="contractor_name", blank=True, verbose_name='Подрядчик')
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
