#coding: utf-8
from django.contrib import admin
from .models import Order, Psd, Insta
from users.models import DUser

#class OrderAdmin(admin.ModelAdmin):
    #filter_horizontal = ('members',)

class InstaAdmin(admin.ModelAdmin):
	list_display = ('dep', 'insta_id',)

class PsdAdmin(admin.ModelAdmin):
	list_display = ('name', 'contractor',)
	list_filter = ('contractor',) 

admin.site.register(Order) #OrderAdmin)
admin.site.register(Psd, PsdAdmin)
admin.site.register(Insta, InstaAdmin)