#coding: utf-8
from django.db import models
from users.models import DUser

class Insta(models.Model):
    insta_id = models.CharField(max_length=15, verbose_name='User ID')
    dep = models.ForeignKey(DUser, related_name='rayon')
  
    class Meta:
        ordering = ['dep',]