#coding: utf-8
from django.db import models
from users.models import DUser

class Insta(models.Model):
    insta_id = models.CharField(max_length=15, verbose_name='User ID')
    dep = models.ForeignKey(DUser, related_name='rayon')
  
    class Meta:
        ordering = ['dep',]


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



CONT = (
    ('121', 'ИПТС Транспроект'),
    ('123', 'ООО «Экодор»'),
    ('124', 'ЗАО «Дагдорпроект»'), 
    ('125', 'ООО «Дорстройпроект»'),
)

class Psd(models.Model):
    name = models.CharField(max_length=512, verbose_name='Объект')
    price = models.FloatField(verbose_name='Стоимость')
    contractor = models.CharField(max_length=4, choices=CONT, verbose_name='Проектировщик')
    exe = models.FloatField(blank=True, verbose_name='Выполнение')
    exe_perc = models.IntegerField(blank=True, default=0, verbose_name='Выполнение, %')
    getsum = models.FloatField(blank=True, verbose_name='Получено')
    exe_getsum = models.IntegerField(blank=True, default=0, verbose_name='Получено, %')
  
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'ПСД'
        verbose_name_plural = 'ПСД'
        ordering = ['name', ]



class Weather(models.Model):
    putdate = models.DateTimeField(auto_now_add=True)
    sost = models.CharField(max_length=50)
    temp = models.CharField(max_length=10)
    pr_r = models.CharField(max_length=100)
    pr_m = models.CharField(max_length=100)
    works = models.TextField(blank=True)
    rayon = models.ForeignKey(DUser, related_name='org')
  
    class Meta:
        ordering = ['-putdate',]

class WeatherCurrent(models.Model):
    putdate = models.DateTimeField(auto_now=True)
    sost = models.CharField(max_length=50)
    temp = models.CharField(max_length=10)
    pr_r = models.CharField(max_length=100)
    pr_m = models.CharField(max_length=100)
    works = models.TextField(blank=True)
    rayon = models.ForeignKey(DUser, related_name='dep')

    class Meta:
        ordering = ['id',]



class Work(models.Model):
    cont = models.IntegerField()
    road = models.IntegerField()
    works = models.TextField()
    tech = models.TextField(blank=True)
    pers = models.CharField(max_length=100, blank=True)
    putdate = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-putdate',]


class WorkImg(models.Model):
    pic = models.ImageField(max_length=250, upload_to='upload/work')
    work = models.ForeignKey(Work, related_name="pics")


class Machine(models.Model):
    name = models.CharField(max_length=512, verbose_name='Наименование техники') 
    body = models.TextField(blank=True, verbose_name='Описание')
    year_issue = models.CharField(max_length=5, verbose_name='Год выпуска')
    pic_1 = models.ImageField(max_length=250, upload_to='upload/machine', verbose_name='Фотография') 
    putdate = models.DateTimeField(auto_now_add=True)
    dep = models.ForeignKey(DUser, related_name='oao') 
  
    class Meta:
        ordering = ['-putdate',]