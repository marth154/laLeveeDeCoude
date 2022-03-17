from django import forms


class RegisterForms(forms.Form):
    username = forms.CharField(
        label='Your username',
        widget=forms.TextInput(attrs={"placeholder": ("Pseudo")})
    )
    email = forms.CharField(
        label='Your email',
        widget=forms.TextInput(attrs={"placeholder": ("Email")}),
    )
    password = forms.CharField(
        label='Your password',
        widget=forms.PasswordInput(attrs={"placeholder": ("Mot de passe")})
    )


class LoginForms(forms.Form):
    username = forms.CharField(
        label='Your username',
        widget=forms.TextInput(attrs={"placeholder": ("Pseudo")}),
    )
    password = forms.CharField(
        label='Your password',
        widget=forms.PasswordInput(attrs={"placeholder": ("Mot de passe")})
    )
