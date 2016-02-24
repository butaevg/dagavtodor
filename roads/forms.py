#coding: utf-8
from django import forms

class ReportForm(forms.Form):
	name = forms.CharField(
		label='Название', 
		max_length=300, 
		widget=forms.TextInput(attrs={'size': '51'}))

class ReportImgForm(forms.Form):
	pic = forms.ImageField(
		label='Фото', 
		max_length=300, 
		widget=forms.FileInput())