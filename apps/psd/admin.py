#coding: utf-8
from django.contrib import admin
from .models import Psd

class PsdAdmin(admin.ModelAdmin):
	list_display = ('name', 'contractor',)
	list_filter = ('contractor',) 

admin.site.register(Psd, PsdAdmin)