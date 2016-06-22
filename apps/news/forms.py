#coding: utf-8
from django import forms

class NewsImgForm(forms.Form):
	pic = forms.ImageField(
		label='Загрузить фотографии к новости',
		widget=forms.FileInput())