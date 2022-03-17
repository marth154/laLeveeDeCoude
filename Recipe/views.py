from django.shortcuts import render
import requests

def random(request):
    response = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    print(response);
    return render(request, 'random.html', {'response': response})

def formatRecipe(recipe):
    print(recipe)
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        if (ing is not None):
            recipeIngredients.append(ing)
            
    return { 'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'] }

def list(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    parsed = response.json()
    finalList = []
    for i in range(len(parsed['drinks'])):
        finalList.append(formatRecipe(parsed['drinks'][i]))
    context = {
        'recipes': finalList,
    }
    print(finalList)
    # print(context)
    return render(request, 'recipe-list.html', context)
