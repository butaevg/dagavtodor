#coding: utf-8
from django.contrib import admin
from .models import Section, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'section',)
	list_filter = ('section',) 
	ordering = ('title',)
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Section)
admin.site.register(Page, PageAdmin)