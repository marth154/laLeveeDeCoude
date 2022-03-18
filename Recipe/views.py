from django.shortcuts import render
import requests
from django.http import HttpResponse, Http404

from Recipe.forms import SearchForms


def random(request):
    response = requests.get(
        'http://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    print(response)
    return render(request, 'random.html', {'response': response})


def formatRecipe(recipe):
    # print(recipe)
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        if (ing is not None):
            recipeIngredients.append(ing)

    return {'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'], 'strDrinkThumb': recipe['strDrinkThumb']}


def list(request):
    form = SearchForms()
    if request.method == "POST":
        query = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + \
            request.POST.get("name")
        response = requests.get(query)
        parsed = response.json()

        if parsed['drinks'] is not None:
            finalList = []
            for i in range(len(parsed['drinks'])):
                finalList.append(formatRecipe(parsed['drinks'][i]))
            context = {
                'form': form,
                'recipes': finalList,
            }
        else:
            context = {
                'form': form, 
            }
    else:
        response = requests.get(
            'https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
        parsed = response.json()
        finalList = []
        for i in range(len(parsed['drinks'])):
            finalList.append(formatRecipe(parsed['drinks'][i]))
        context = {
            'form': form,
            'recipes': finalList,
        }

    return render(request, 'recipe-list.html', context)
