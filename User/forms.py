from django import forms


class RegisterForms(forms.Form):
    username = forms.CharField(
        label='Pseudo',
        widget=forms.TextInput(attrs={"placeholder": ("Pseudo")})
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={"placeholder": ("Email")}),
    )
    password = forms.CharField(
        label='Mot de passe ',
        widget=forms.PasswordInput(attrs={"placeholder": ("Mot de passe")})
    )


class LoginForms(forms.Form):
    username = forms.CharField(
        label='Pseudo',
        widget=forms.TextInput(attrs={"placeholder": ("Pseudo")}),
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={"placeholder": ("Mot de passe")})
    )
