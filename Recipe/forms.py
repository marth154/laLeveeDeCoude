from dataclasses import fields
from pickle import FALSE
from django.db import models
from django import forms
from django.shortcuts import render
import requests

from Recipe.models import Recipe

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


class Test(models.Model):
    categoriesList = getCategories()
    glassesList = getGlasses()
    alcoholicList = getAlcoholics()
    ingredientsList = getIngredients()

    name = models.CharField(max_length=250)
    # categories = models.CharField(choices = categoriesList, max_length=300)
    # glasses = models.CharField(choices = glassesList, max_length=300)
    # alcoholics = models.CharField(choices = alcoholicList, max_length=300)
    # ingredients = models.CharField(choices = ingredientsList, max_length=300)

class CreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', )
