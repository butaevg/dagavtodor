#coding: utf-8
from django import forms
from .models import Road 
from datetime import datetime


class WorkbookForm(forms.Form):
	road = forms.ModelChoiceField(
		label='Выберите объект из выпадающего списка', 
		queryset=Road.objects.none(), 
		initial=0, 
		required = True)
	file = forms.FileField(
		label='Файл',
		widget=forms.FileInput(), 
		required = True)
	putdate = forms.DateField(
		label='Дата',
		widget=forms.TextInput(attrs={'class': 'datepicker'}), 
		initial = datetime.today().strftime('%d.%m.%Y'), 
		required = True)

	def __init__(self, *args, **kwargs):
		user_id = kwargs.pop('user_id', None)
		super(WorkbookForm, self).__init__(*args, **kwargs)
		self.fields['road'].queryset = Road.objects.filter(dep=user_id)
