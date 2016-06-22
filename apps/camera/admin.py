#coding: utf-8
from django.contrib import admin
from .models import Cam3g, CamIp

class Cam3gAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip',)
	list_filter = ('hide',) 

class CamIpAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip',)
	list_filter = ('hide',) 

admin.site.register(Cam3g, Cam3gAdmin)
admin.site.register(CamIp, CamIpAdmin)