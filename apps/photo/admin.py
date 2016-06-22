#coding: utf-8
from django.contrib import admin

from .models import PhotoCat, Photo

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('image_tag', 'cat',)
	#readonly_fields = ('image_tag',)

admin.site.register(PhotoCat)
admin.site.register(Photo, PhotoAdmin)