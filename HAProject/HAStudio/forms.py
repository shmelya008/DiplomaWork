from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, label='Номер телефона', help_text='Номер телефона в формате +7 (999) ...')
    requested_service = forms.CharField(max_length=20, required=True, label='Запрашиваемая услуга', help_text='Введите название желаемой услуги')
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Одна большая буква и т.д.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'requested_service', 'password1', 'password2')

