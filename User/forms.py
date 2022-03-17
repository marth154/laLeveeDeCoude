from django import forms


class RegisterForms(forms.Form):
    # username = forms.CharField(label='Your pseudo', validators=[validate_username])
    # email = forms.CharField(label='Your email', validators=[validate_email])
    # password = forms.CharField(label='Your password',widget=forms.PasswordInput())
    username = forms.CharField(label='Your pseudo')
    email = forms.CharField(label='Your email')
    password = forms.CharField(label='Your password', widget=forms.PasswordInput())
