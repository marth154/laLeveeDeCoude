from pickle import FALSE
from urllib import response
from django import forms
from django.shortcuts import render
import requests
from Ingredient.models import Ingredient

from Recipe.models import Category, Glass

def getCategories():
    categories = [('' , '')]

    response = Category.objects.all()
    for i in range(len(response)):
        categories.append((response[i].id, response[i].name))

    return categories

def getGlasses():
    glasses = [('' , '')]
    
    response = Glass.objects.all()
    for i in range(len(response)):
        glasses.append((response[i].id  , response[i].name))

    return glasses

def getIngredients():
    ingredients = [('' , '')]
    
    response = Ingredient.objects.all()
    for i in range(len(response)):
        ingredients.append((response[i].name, response[i].name))

    return ingredients

class SearchForms(forms.Form):
    categoriesList = getCategories()
    glassesList = getGlasses()
    ingredientslist = getIngredients()

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

    alcoholic = forms.ChoiceField(
        widget=forms.Select,
        choices=[
            ('', ''),
            ('True', 'Alcoholic'),
            ('False', 'Non Alcoholic'),
            # ('Optional alcohol', 'Optional alcohol'),
        ],
        required = False
    )

    ingredients = forms.ChoiceField(
        widget= forms.Select,
        choices = ingredientslist,
        required = False
    )
