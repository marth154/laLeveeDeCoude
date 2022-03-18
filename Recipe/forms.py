from django import forms


class SearchForms(forms.Form):
    name = forms.CharField(
        label='Nom de cocktail',
        widget=forms.TextInput(attrs={"placeholder": ("Nom de cocktail")})
    )
