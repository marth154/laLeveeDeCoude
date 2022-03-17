from django import forms
from validators.register import validate_username

class RegisterForms(forms.Form):
    username = forms.CharField(label='Your username', validators=[validate_username])
    email = forms.CharField(label='Your email')
    password = forms.CharField(label='Your password',widget=forms.PasswordInput())
    # username = forms.CharField(label='Your pseudo')
    # email = forms.CharField(label='Your email')
    # password = forms.CharField(label='Your password', widget=forms.PasswordInput())
