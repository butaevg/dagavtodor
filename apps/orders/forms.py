#coding: utf-8
from django import forms

class OrderExecForm(forms.Form):
	process = forms.CharField(
		label='Что выполнено', 
		widget=forms.Textarea(attrs={'rows': '7', 'cols': '70'})) 
	process_perc = forms.CharField(
		label='Процент выполнения', 
		widget=forms.TextInput(attrs={'size': '10'}))