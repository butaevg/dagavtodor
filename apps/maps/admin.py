#coding: utf-8
from django.contrib import admin
from .models import Map

class MapAdmin(admin.ModelAdmin):
	list_display = ('rayon',)
	ordering = ('rayon',)

admin.site.register(Map, MapAdmin)