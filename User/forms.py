from django import forms


class RegisterForms(forms.Form):
    username = forms.CharField(label='Your username')
    email = forms.CharField(label='Your email')
    password = forms.CharField(
        label='Your password', widget=forms.PasswordInput())


class LoginForms(forms.Form):
    username = forms.CharField(label='Your username')
    password = forms.CharField(
        label='Your password', widget=forms.PasswordInput())
