#coding: utf-8
from django.db import models 
from datetime import datetime

class News(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    source = models.CharField(max_length=100, blank=True, verbose_name='Источник')
    body = models.TextField(verbose_name='Текст')
    mainpic = models.ImageField(max_length=250, upload_to='news/%Y-%m-%d/', verbose_name='Картинка на главной')
    putdate = models.DateTimeField(verbose_name='Дата', default=datetime.now) 

    def get_absolute_url(self):
        return '/news/upload_pic/%i/' % self.id

    class Meta:
        ordering = ['-putdate']


class NewsImg(models.Model):
    pic = models.ImageField(max_length=250, upload_to='news/%Y-%m-%d/', verbose_name='Фотографии к новости')
    post = models.ForeignKey(News, related_name="pics")

