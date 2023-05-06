from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from orderfood.models import Employee


class PartialForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label='Сотрудник')
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': ''}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': ''}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': ''}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': ''}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': ''}))

