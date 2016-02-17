#coding: utf-8
from django.contrib import admin
from .models import DocsCat, Doc

class DocAdmin(admin.ModelAdmin):
	list_display = ('name', 'cat',)

admin.site.register(DocsCat)
admin.site.register(Doc, DocAdmin)