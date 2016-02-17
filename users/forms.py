#coding: utf-8
from django import forms
from .models import DUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин: ', 
        max_length=20, 
        widget=forms.TextInput(attrs={'size': '20'}))
    password = forms.CharField(
        label='Пароль: ', 
        max_length=20, 
        widget=forms.PasswordInput(attrs={'size': '20'}))


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Пароль (еще раз)', widget=forms.PasswordInput)

    class Meta:
        model = DUser
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label= ('Пароль'),
        help_text= ('Пароли не хранятся в открытом виде, поэтому '
                    'он здесь не отображается. ' 
                    'Можно изменить пароль, используя <a href=\"password/\">эту форму</a>.'))

    class Meta:
        model = DUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]