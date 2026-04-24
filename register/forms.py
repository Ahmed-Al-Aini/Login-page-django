from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="username", max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    password1 = forms.CharField(label="password1", max_length=200,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="password2", max_length=200,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter verify password'}))
    gender= forms.ChoiceField(choices=[('male','male'),('female','female')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','gender']



class LoginForm(UserCreationForm):
    username = forms.CharField(label="username",max_length=200,widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    password = forms.CharField(label="password",max_length=200,widget=forms.PasswordInput(attrs={'placeholder':'Enter password','autocomplete':'current-password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


