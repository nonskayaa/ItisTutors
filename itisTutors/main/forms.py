from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    group_number = forms.CharField\
        (max_length=6, required=True,
         label='Номер группы')

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2= forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    username = forms.CharField(
        label='Никнейм',
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'group_number', 'email', 'password1', 'password2', )