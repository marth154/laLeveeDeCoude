from operator import concat
from django.shortcuts import render
import requests

from requests.adapters import HTTPAdapter
from urllib3.util import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def random(request):
    response = session.get('http://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    print('🚀 ~ file: views.py ~ line 7 ~ response', response);
    parsedResponse = formatRecipe(response['drinks'][0])
    return render(request, 'random.html', {'response': parsedResponse})

def formatRecipe(recipe):
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        measure = recipe['strMeasure' + str(i)]
        if ((ing is not None and measure is not None) and (ing != '' and measure != '')):
            recipeIngredients.append(ing + ' : ' + measure)
            
    return { 'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'], 'strDrinkThumb': recipe['strDrinkThumb'] }

def list(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    parsed = response.json()
    finalList = []
    for i in range(len(parsed['drinks'])):
        finalList.append(formatRecipe(parsed['drinks'][i]))
    context = {
        'recipes': finalList,
    }
    return render(request, 'recipe-list.html', context)
