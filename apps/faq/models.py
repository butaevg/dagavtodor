#coding: utf-8
from django.db import models 
from datetime import datetime

class Question(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО полностью *')
    city = models.CharField(blank=True, max_length=100, verbose_name='Город') 
    address = models.CharField(blank=True, max_length=200, verbose_name='Почтовый адрес *')
    email = models.EmailField(blank=True, verbose_name='Адрес электр. почты')
    msg = models.TextField(verbose_name='Текст обращения *')
    img = models.ImageField(blank=True, upload_to='faq/%Y-%m-%d/', verbose_name='Прилагаемoе фото')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    putdate = models.DateField(auto_now_add=True) 
    hide = models.BooleanField(default=True)

    class Meta:
        ordering = ['-putdate']