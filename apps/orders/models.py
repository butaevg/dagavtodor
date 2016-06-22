#coding: utf-8
from django.db import models
from users.models import DUser

class Order(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    body = models.TextField(verbose_name='Описание')
    putdate = models.DateField(verbose_name='Дата')
    expiredate = models.DateField(verbose_name='Срок')    
    hide = models.BooleanField(default=False)
    members = models.ManyToManyField(DUser, verbose_name='Исполнители')

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'поручение'
        verbose_name_plural = 'Поручения'
        ordering = ['-putdate']

class OrderExec(models.Model):
    process = models.TextField(verbose_name='Что сделано')
    process_perc = models.IntegerField(verbose_name='Процент')
    putdate = models.DateField(auto_now_add=True)  
    member = models.ForeignKey(DUser, related_name='member')
    order_id = models.IntegerField()