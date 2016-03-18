#coding: utf-8
from django.db import models

TYPE_OF_ORG = (
    ('dep', 'Дорожно-эксплуатационные предприятия'),
    ('vne', 'Внешние подрядчики'),
    ('uch', 'Учреждения'), 
    ('ao', 'Акционерные общества'),
)

class Org(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название') 
    body = models.TextField(blank=True, verbose_name='Текст')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефоны')
    email = models.EmailField(max_length=100, blank=True, verbose_name='E-mail')
    site = models.CharField(max_length=100, blank=True, verbose_name='Сайт')
    director = models.CharField(max_length=150, verbose_name='Руководитель')
    cat = models.CharField(max_length=3, choices=TYPE_OF_ORG, verbose_name='Тип')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'организацию'
        verbose_name_plural = 'Организации'

class Info(models.Model):
    icon = models.CharField(max_length=50)
    catname = models.CharField(max_length=100)
    org_id = models.IntegerField()
    cat = models.IntegerField()
