#coding: utf-8
from django.contrib import admin
from .models import Advert, PhotoCat, Photo

class AdvertAdmin(admin.ModelAdmin):
	list_display = ('name', 'putdate',)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('image_tag', 'cat',)
	#readonly_fields = ('image_tag',)

admin.site.register(Advert, AdvertAdmin)
admin.site.register(PhotoCat)
admin.site.register(Photo, PhotoAdmin)