#coding: utf-8
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=300, verbose_name='Отдел')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'отдел'
        verbose_name_plural = 'Отделы'


class Employee(models.Model):
    position = models.CharField(max_length=512, verbose_name='Должность')
    name = models.CharField(max_length=512, verbose_name='ФИО')
    phone = models.CharField(max_length=256, verbose_name='Телефон')
    dep = models.ForeignKey(Department, related_name='dep', verbose_name='Отдел')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'