#coding: utf-8
from django import forms

class JournalForm(forms.Form):

	work_type_pos_smeta = forms.CharField(
		label='Номер<br> позиции<br> по смете', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '5', 'readonly': 'readonly'}))

	work_type_name = forms.CharField(
		label='Наименование работ', 
		required=False, 
		widget=forms.Textarea(attrs={'rows': '5', 'cols': '30', 'readonly': 'readonly'})) 

	work_type_num_unit = forms.CharField(
		label='Номер<br> единичной<br> расценки', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '1', 'readonly': 'readonly'})) 

	work_type_unit = forms.CharField(
		label='Единица<br> измерения', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '5', 'readonly': 'readonly'}))

	work_type_price_unit = forms.CharField(
		label='Цена за<br>единицу<br> измерения', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '5', 'readonly': 'readonly'}))

	count_all = forms.CharField(
		label='Количество<br> с начала<br> квартала', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '6', 'maxlength': '10'}))
	count_current = forms.CharField(
		label='Количество<br> за сегодня', 
		required=False, 
		widget=forms.TextInput(attrs={'size': '6', 'maxlength': '10'}))
	val_all = forms.CharField(
		label='Стоимость<br> с начала<br> квартала', 
		required=False,
		widget=forms.TextInput(attrs={'size': '6', 'maxlength': '10'}))
	val_current = forms.CharField(
		label='Стоимость<br> за сегодня', 
		required=False,
		widget=forms.TextInput(attrs={'size': '6', 'maxlength': '10'}))
	position = forms.CharField(
		label='Адрес<br> проведения<br> работ',  
		required=False,
		widget=forms.TextInput(attrs={'size': '20', 'maxlength': '100'}))

	work_type_id = forms.CharField( 
			widget=forms.TextInput(attrs={'type': 'hidden'}))