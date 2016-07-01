#coding: utf-8
from django.contrib import admin
from .models import Road

class RoadAdmin(admin.ModelAdmin):
	list_display = ('name', 'dep',)
	list_filter = ('dep',) 

admin.site.register(Road, RoadAdmin)