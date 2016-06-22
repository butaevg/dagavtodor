#coding: utf-8
from django.contrib import admin
from .models import Advert

class AdvertAdmin(admin.ModelAdmin):
	list_display = ('name', 'putdate',)

admin.site.register(Advert, AdvertAdmin)