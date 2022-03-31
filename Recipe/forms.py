from abc import abstractmethod, abstractproperty
from dataclasses import fields
from pickle import FALSE
from django.db import models
from django import forms
from django.shortcuts import render
import requests
from Ingredient.models import Ingredient

from Recipe.models import Category, Glass

from Recipe.models import Recipe

from Recipe.models import Category, Glass, Recipe
from User.views import get_ingredient


def getCategories():
    categories = [('', '')]
    get_category = Category.objects.all()
    for category in get_category:
        categories.append(
            (category.name, category.name))
    return categories


def getGlasses():
    glasses = [('', '')]
    get_glasses = Glass.objects.all()
    for glass in get_glasses:
        glasses.append((glass.name, glass.name))
    return glasses


def getIngredients():
    ingredients = []
    get_ingredients = Ingredient.objects.all()
    for ingredient in get_ingredients:
        ingredients.append(
            (ingredient.name, ingredient.name))
    return ingredients


def getAlcoholics():
    alcoholic = [('', '')]
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/list.php?a=list').json()

    for i in range(len(response['drinks'])):
        alcoholic.append(
            (response['drinks'][i]['strAlcoholic'], response['drinks'][i]['strAlcoholic']))
    return alcoholic


class SearchForms(forms.Form):
    categoriesList = getCategories()
    glassesList = getGlasses()
    ingredientslist = getIngredients()

    name = forms.CharField(
        label='Cocktail name',
        widget=forms.TextInput(attrs={"placeholder": ("Cocktail name")}),
        required=False
    )

    categories = forms.ChoiceField(
        widget=forms.Select,
        choices=categoriesList,
        required=False,
    )

    glasses = forms.ChoiceField(
        widget=forms.Select,
        choices=glassesList,
        required=False
    )

    alcoholic = forms.ChoiceField(
        widget=forms.Select,
        choices=[
            ('', ''),
            ('True', 'Alcoholic'),
            ('False', 'Non Alcoholic'),
            # ('Optional alcohol', 'Optional alcohol'),
        ],
        required=False
    )

    ingredients = forms.ChoiceField(
        widget=forms.Select,
        choices=ingredientslist,
        required=False
    )


class CreateRecipe(forms.Form):
    categoriesList = getCategories()
    glassesList = getGlasses()
    alcoholicList = getAlcoholics()
    ingredientsList = getIngredients()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     ingredientsList = getIngredients()

    #     for i in range(len(ingredientsList) - 1):
    #         field_name = 'ingredient_%s' % (i,)
    #         self.fields[field_name] = forms.MultipleChoiceField(
    #             required=False,
    #             widget=forms.CheckboxSelectMultiple,
    #             choices=ingredientsList
    #         )

    # def get_ingredient_fields(self):
    #     for field_name in self.fields:
    #         if field_name.startswith('ingredient_'):
    #             yield self[field_name]

    name = forms.CharField(
        label='Name of recipe',
        widget=forms.TextInput(attrs={"placeholder": ("Name of recipe")})
    )
    categories = forms.ChoiceField(
        widget=forms.Select,
        choices=categoriesList,
    )
    glasses = forms.ChoiceField(
        widget=forms.Select,
        choices=glassesList,
    )
    alcoholic = forms.ChoiceField(
        widget=forms.Select,
        choices=[
            ('', ''),
            ('True', 'Alcoholic'),
            ('False', 'No Alcoholic'),
            # ('Optional alcohol', 'Optional alcohol'),
        ],
    )

    # ingredients = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.MultiWidget(
    #         widgets=[
    #             forms.CheckboxSelectMultiple,
    #             forms.TextInput(
    #                 attrs={"placeholder": ("Quantity")}
    #             )
    #         ]
    #     ),
    #     widget=IngredientQuantity(),
    #     choices=ingredientsList
    # )
    ingredients = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ingredientsList
    )
    steps = forms.CharField(
        label='Steps',
        widget=forms.Textarea(attrs={"placeholder": ("Steps")})
    )
    is_shared = forms.ChoiceField(
        label='Is shared',
        widget=forms.Select,
        choices=[
            ('False', 'No'),
            ('True', 'Yes'),
        ]
    )
