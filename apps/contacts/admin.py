#coding: utf-8
from django.contrib import admin
from .models import Department, Employee

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'dep',)

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)