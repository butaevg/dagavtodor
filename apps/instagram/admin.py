#coding: utf-8
from django.contrib import admin
from .models import Insta

class InstaAdmin(admin.ModelAdmin):
	list_display = ('dep', 'insta_id',)

admin.site.register(Insta, InstaAdmin)