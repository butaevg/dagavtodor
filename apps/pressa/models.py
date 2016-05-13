#coding: utf-8
from django.db import models

class Advert(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    putdate = models.DateField(verbose_name='Дата')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-putdate']


class Article(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    pic = models.ImageField(max_length=250, blank=True, upload_to='articles/%Y-%m-%d/', verbose_name='Фото')
    putdate = models.DateField(verbose_name='Дата')
    source = models.CharField(max_length=512, blank=True, verbose_name='Ссылка на источник')
    source_name = models.CharField(max_length=100, blank=True, verbose_name='Источник')
    
    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-putdate']


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

        
class Post(models.Model):
    name = models.CharField(max_length=512, verbose_name='Заголовок')
    source = models.CharField(max_length=100, blank=True, verbose_name='Источник')
    body = models.TextField(verbose_name='Текст')
    mainpic = models.ImageField(max_length=250, upload_to='news/%Y-%m-%d/', verbose_name='Картинка на главной')
    putdate = models.DateTimeField(verbose_name='Дата')
    
    def get_absolute_url(self):
        return '/pressa/post/upload_pic/%i/' % self.id

    class Meta:
        ordering = ['-putdate']


class PostImg(models.Model):
    pic = models.ImageField(max_length=250, upload_to='news/%Y-%m-%d/', verbose_name='Фотографии к новости')
    post = models.ForeignKey(Post, related_name="pics")


class Question(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя *')
    city = models.CharField(blank=True, max_length=100, verbose_name='Город')
    email = models.EmailField(blank=True, verbose_name='Адрес электр. почты')
    msg = models.TextField(verbose_name='Текст обращения *')
    img = models.ImageField(blank=True, upload_to='faq/%Y-%m-%d/', verbose_name='Прилагаемoе фото')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    putdate = models.DateField(auto_now_add=True) 
    hide = models.BooleanField(default=True)

    class Meta:
        ordering = ['-putdate']