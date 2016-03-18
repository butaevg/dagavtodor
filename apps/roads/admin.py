#coding: utf-8
from django.contrib import admin
from .models import Road, Map, Cam3g, CamIp

class RoadAdmin(admin.ModelAdmin):
	list_display = ('name', 'contractor',)
	list_filter = ('cat', 'onsite', 'report', 'complete',) 

class MapAdmin(admin.ModelAdmin):
	list_display = ('rayon',)
	ordering = ('rayon',)

class Cam3gAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip',)
	list_filter = ('hide',) 

class CamIpAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip',)
	list_filter = ('hide',) 

admin.site.register(Road, RoadAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Cam3g, Cam3gAdmin)
admin.site.register(CamIp, CamIpAdmin)