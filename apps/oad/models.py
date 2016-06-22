#coding: utf-8
from django.db import models
from datetime import datetime

class WorkType(models.Model): 
    pos_smeta = models.IntegerField(default=0)
    name = models.CharField(max_length=512, verbose_name='Наименование работ') 
    num_unit = models.IntegerField(blank=True, null=True, verbose_name='Номер единич. расценки') 
    unit = models.CharField(max_length=20, verbose_name='Единица измерения') 
    price_unit = models.CharField(max_length=20, verbose_name='Цена за ед. измерения') 

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'работу'
        verbose_name_plural = 'Работы'


class Journal(models.Model): 
    work_type = models.ForeignKey(WorkType, related_name="work") 
    count_all = models.CharField(max_length=20)  
    count_current = models.CharField(max_length=20)   
    val_all = models.CharField(max_length=20)   
    val_current = models.CharField(max_length=20)   
    position = models.CharField(max_length=100)   
    putdate = models.DateField(default=datetime.now)
    