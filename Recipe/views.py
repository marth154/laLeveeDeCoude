from operator import concat
from django.shortcuts import render
import requests

from Recipe.forms import SearchForms

def random(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
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

def getId(n):
    return n.idDrink

def list(request):
    form = SearchForms()
    if request.method == "POST":
        if request.POST.get("name"):
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

        elif request.POST.get("categories"):
            query = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=' + \
                request.POST.get("categories")
            response = requests.get(query)
            parsed = response.json()
            
            drinksIds = []
            if parsed['drinks'] is not None:
                for i in range(len(parsed['drinks'])):
                    drinksIds.append(parsed['drinks'][i]['idDrink'])
                finalList = []
                for i in range(len(drinksIds)):
                    responseDrink = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()                    
                    finalList.append(formatRecipe(responseDrink['drinks'][0]))
                context = {
                    'form': form,
                    'recipes': finalList,
                }
            else:
                context = {
                    'form': form, 
                }

        elif request.POST.get("glasses"):
            query = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?g=' + \
                request.POST.get("glasses")
            response = requests.get(query)
            parsed = response.json()
            
            drinksIds = []
            if parsed['drinks'] is not None:
                for i in range(len(parsed['drinks'])):
                    drinksIds.append(parsed['drinks'][i]['idDrink'])
                finalList = []
                for i in range(len(drinksIds)):
                    responseDrink = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()                    
                    finalList.append(formatRecipe(responseDrink['drinks'][0]))
                context = {
                    'form': form,
                    'recipes': finalList,
                }
            else:
                context = {
                    'form': form, 
                }

        elif request.POST.get("alcoholics"):
            query = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=' + \
                request.POST.get("alcoholics")
            response = requests.get(query)
            parsed = response.json()
            
            drinksIds = []
            if parsed['drinks'] is not None:
                for i in range(len(parsed['drinks'])):
                    drinksIds.append(parsed['drinks'][i]['idDrink'])
                finalList = []
                for i in range(len(drinksIds)):
                    responseDrink = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()                    
                    finalList.append(formatRecipe(responseDrink['drinks'][0]))
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
