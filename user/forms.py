from django import forms
from .models import User
from time import sleep
from django.core.mail import send_mail

class LoginForm(forms.Form):
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Нікнейм'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'nickname', 'address', 'city', 'card_number', 'email', 'language', 'phone', 'sex', 'birthday', 'password', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'datepicker1',
                'autocomplete': 'off'}),
            'language': forms.RadioSelect(attrs={'class': 'ml-2'}),
            'sex': forms.RadioSelect(attrs={'class': 'ml-2'})
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Паролі не співпадають')
        return cd['password2']
