#coding: utf-8
from django.contrib import admin
from .models import Order

#class OrderAdmin(admin.ModelAdmin):
    #filter_horizontal = ('members',)

admin.site.register(Order) #OrderAdmin)