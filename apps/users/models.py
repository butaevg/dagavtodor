#coding: utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Раздел')
    name_menu = models.CharField(max_length=150, verbose_name='Название для меню')
    url = models.CharField(max_length=150, verbose_name='Ссылка')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'Разделы'

class UserCat(models.Model):
    name = models.CharField(max_length=100, verbose_name='Группа')
    cats = models.ManyToManyField(Category, verbose_name='Разделы')

    def __unicode__(self):
        return self.name
        
    class Meta:
        db_table = 'users_group'
        verbose_name = 'группу'
        verbose_name_plural = 'Группы'


class DUserManager(BaseUserManager):
    def create_user(self, username, password = None, **kwargs):
        if not username:
            raise ValueError(_('Имя пользователя обязательно'))
 
        user = self.model(
            username = username,
            **kwargs
        )
 
        user.set_password(password)
        user.save(using = self._db)
        return user
 
    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username = username,
            password = password,
            **kwargs
        )
        user.is_admin = True
        user.save(using = self._db)
        return user


class DUser(AbstractBaseUser):
    name = models.CharField(max_length = 180, verbose_name = 'Имя')
    username = models.CharField(max_length = 80, unique = True, verbose_name = 'Логин')
    #password = models.CharField(max_length = 80, verbose_name = 'password')
    fullname = models.CharField(max_length = 150, verbose_name = 'Полное имя')
    cat = models.ForeignKey(UserCat, null=True, verbose_name = 'Группа')
    insta = models.CharField(max_length = 150, blank=True, verbose_name = 'Instagram')
    is_admin = models.BooleanField(default = False, verbose_name = 'Администратор')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name',]
    
    objects = DUserManager()
 
    def get_short_name(self):
        return self.username
 
    def __unicode__(self):
        return self.fullname
 
    def has_perm(self, perm, obj=None):
        return True
 
    def has_module_perms(self, app_label):
        return True
 
    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
    	db_table = 'users'
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'