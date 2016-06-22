#coding: utf-8
from django import forms

class PsdExeForm(forms.Form):
	price = forms.CharField(
		label='Стоимость ', 
		widget=forms.TextInput(attrs={'size': '15'}))
	exe = forms.CharField(
		label='Выполнение из ', 
		widget=forms.TextInput(attrs={'size': '15'}))
	getsum = forms.CharField(
		label='Полученно из ', 
		widget=forms.TextInput(attrs={'size': '15'}))