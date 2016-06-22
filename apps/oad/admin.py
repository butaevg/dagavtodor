#coding: utf-8
from django.contrib import admin
from .models import WorkType

class WorkTypeAdmin(admin.ModelAdmin):
	list_display = ('pos_smeta', 'name', 'unit', 'price_unit',)

admin.site.register(WorkType, WorkTypeAdmin)