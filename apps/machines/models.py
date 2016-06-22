#coding: utf-8
from django.db import models
from users.models import DUser

class Machine(models.Model):
    name = models.CharField(max_length=512, verbose_name='Наименование техники') 
    body = models.TextField(blank=True, verbose_name='Описание')
    year_issue = models.CharField(max_length=5, verbose_name='Год выпуска')
    pic_1 = models.ImageField(upload_to='machine', verbose_name='Фото 1') 
    pic_2 = models.ImageField(upload_to='machine', verbose_name='Фото 2', blank=True) 
    pic_3 = models.ImageField(upload_to='machine', verbose_name='Фото 3', blank=True) 
    pic_4 = models.ImageField(upload_to='machine', verbose_name='Фото 4', blank=True)
    pic_5 = models.ImageField(upload_to='machine', verbose_name='Фото 5', blank=True)
    putdate = models.DateTimeField(auto_now_add=True)
    dep = models.ForeignKey(DUser, related_name='owner') 
    working = models.BooleanField(default=True)
  
    class Meta:
        ordering = ['dep',]