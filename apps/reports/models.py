#coding: utf-8
from django.db import models
from users.models import DUser


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
    pic = models.ImageField(max_length=250, upload_to='work/%Y-%m-%d/')
    work = models.ForeignKey(Work, related_name="pics")