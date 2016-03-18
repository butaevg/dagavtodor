#coding: utf-8
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import DUser, Category, UserCat
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'username', 'cat', 'last_login')
    list_filter = ('cat_id',) 
    fieldsets = (
        ('Основные данные', {
            'fields': ('username', 'password', 'cat', 'is_admin')}),
        ('Дополнительные данные', {
            'classes': ('wide',),
            'fields': ('name', 'fullname', 'insta')}
        ),
    )
    add_fieldsets = (
        ('Основные данные', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'cat', 'is_admin')}
        ),
        ('Дополнительные данные', {
            'classes': ('wide',),
            'fields': ('name', 'fullname', 'insta')}
        ),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_menu', 'url',)
    ordering = ('name',)

class UserCatAdmin(admin.ModelAdmin):
    filter_horizontal = ('cats',)

admin.site.register(DUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserCat, UserCatAdmin)