#coding: utf-8
from django import forms
from roads.models import Road

class OrderExecForm(forms.Form):
	process = forms.CharField(
		label='Что выполнено', 
		widget=forms.Textarea(attrs={'rows': '7', 'cols': '70'})) 
	process_perc = forms.CharField(
		label='Процент выполнения', 
		widget=forms.TextInput(attrs={'size': '10'}))


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


class WeatherDateForm(forms.Form):
	putdate = forms.CharField(
		label='Дата: ', 
		widget=forms.TextInput(attrs={'class': 'datepicker'}), 
		required = True)

SOST = (
    ("ясно", "ясно"), 
    ("пасмурно", "пасмурно"),
    ("туман", "туман"),
    ("дождь", "дождь"),
    ("снег", "снег"),
)

PR = (
    ("покрытие дорог сухое", "покрытие дорог сухое"),
    ("покрытие дорог мокрое", "покрытие дорог мокрое"),
    ("снег", "снег"),
    ("снежный накат", "снежный накат"),
    ("снежный накат обраб. ПГМ", "снежный накат обраб. ПГМ"),
    ("слаб. гололедица", "слаб. гололедица"), 
    ("гололед", "гололед"), 
    ("гололед обраб. ПГМ", "гололед обраб. ПГМ"), 
    ("подсыпаны ПГМ", "подсыпаны ПГМ"),
)

class WeatherForm(forms.Form):
	sost = forms.CharField(
		label='Состояние', 
		widget=forms.Select(choices=SOST))
	temp = forms.CharField(
		label='Температура окружающей среды, С', 
		widget=forms.TextInput(attrs={'size': '6', 'maxlength': '3'}))
	pr_r = forms.CharField(
		label='Проезжаемость на дорогах респ. значения', 
		widget=forms.Select(choices=PR))
	pr_m = forms.CharField(
		label='Проезжаемость на дорогах местн. значения', 
		widget=forms.Select(choices=PR))
	works = forms.CharField(
		label='Проводимые работы',
		widget=forms.Textarea(attrs={'rows': '8', 'cols': '60'})) 


class WorkForm(forms.Form):
	road = forms.ModelChoiceField(
		label='Выберите объект из выпадающего списка', 
		queryset=Road.objects.none(), 
		initial=0)
	works = forms.CharField(
		label='Наименование выполненных работ и пикетажное положение',
		widget=forms.Textarea(attrs={'rows': '10', 'cols': '60'})) 
	tech = forms.CharField(
		label='Наименование техники (механизмов) и количество единиц в смену',
		widget=forms.Textarea(attrs={'rows': '5', 'cols': '60'}))
	pers = forms.CharField(
		label='Количество работников в смену', 
		widget=forms.TextInput(attrs={'size': '61'})) 

	def __init__(self, *args, **kwargs):
		user_id = kwargs.pop('user_id', None)
		super(WorkForm, self).__init__(*args, **kwargs)
		self.fields['road'].queryset = Road.objects.filter(contractor=user_id)

class WorkImgForm(forms.Form):
	pic = forms.ImageField(
		label='Загрузить фотографии к отчету | Внимание: не больше 10 фотографий!',
		widget=forms.FileInput())


# class MachineForm(forms.Form):
# 	name = forms.CharField(
# 		label='Наименование',
# 		widget=forms.TextInput(attrs={'size': '61'}))  
# 	body = forms.CharField(
# 		label='Описание',
# 		widget=forms.Textarea(attrs={'rows': '5', 'cols': '60'}))
# 	year_issue = forms.CharField(
# 		label='Год выпуска', 
# 		widget=forms.TextInput(attrs={'size': '11'})) 
# 	pic_1 = forms.ImageField(
# 		label='Фотография',
# 		widget=forms.FileInput())