from pickle import FALSE
from django import forms
from django.shortcuts import render
import requests

def getCategories():
    categories = [('' , '')]
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list').json()
    for i in range(len(response['drinks'])):
        categories.append((response['drinks'][i]['strCategory'], response['drinks'][i]['strCategory']))
    return categories

def getGlasses():
    glasses = [('' , '')]
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?g=list').json()
    for i in range(len(response['drinks'])):
        glasses.append((response['drinks'][i]['strGlass'], response['drinks'][i]['strGlass']))
    return glasses

def getIngredients():
    ingredients = [('' , '')]
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list').json()
    for i in range(len(response['drinks'])):
        ingredients.append((response['drinks'][i]['strIngredient1'], response['drinks'][i]['strIngredient1']))
    return ingredients

def getAlcoholics():
    alcoholic = [('' , '')]
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?a=list').json()
    for i in range(len(response['drinks'])):
        alcoholic.append((response['drinks'][i]['strAlcoholic'], response['drinks'][i]['strAlcoholic']))
    return alcoholic

class SearchForms(forms.Form):
    categoriesList = getCategories()
    glassesList = getGlasses()
    alcoholicList = getAlcoholics()

    name = forms.CharField(
        label='Cocktail name',
        widget=forms.TextInput(attrs={"placeholder": ("Cocktail name")}),
        required = False
    )

    categories = forms.ChoiceField(
        widget= forms.Select,
        choices = categoriesList,
        required = False,
    )

    glasses = forms.ChoiceField(
        widget= forms.Select,
        choices = glassesList,
        required = False
    )

    alcoholics = forms.ChoiceField(
        widget= forms.Select,
        choices = alcoholicList,
        required = False
    )
