#coding: utf-8
from django.db import models 
from datetime import datetime

class PhotoCat(models.Model):
    name = models.CharField(max_length=512, verbose_name='Альбом')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'Альбомы' 
        ordering = ['-id']


class Photo(models.Model):
    url = models.ImageField(max_length=250, upload_to='photo', verbose_name='Фото')
    cat = models.ForeignKey(PhotoCat, related_name="cat", verbose_name='Альбом')

    def image_tag(self):
        return u'<img src="/%s" width="120" height="90" />' % (self.url)
    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True
    
    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фотографии'