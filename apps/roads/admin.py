#coding: utf-8
from django.contrib import admin
from .models import Road

class RoadAdmin(admin.ModelAdmin):
	list_display = ('name', 'contractor',)
	list_filter = ('cat', 'onsite', 'report', 'complete',) 

admin.site.register(Road, RoadAdmin)