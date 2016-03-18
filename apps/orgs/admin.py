#coding: utf-8
from django.contrib import admin
from .models import Org

class OrgAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('cat',) 
	ordering = ('name',)

admin.site.register(Org, OrgAdmin)