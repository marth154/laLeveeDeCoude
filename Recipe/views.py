from django.shortcuts import render
from urllib3.util import Retry
import requests
from requests.adapters import HTTPAdapter
from django.http import Http404
from Recipe.models import Recipe, Category, Glass, Ingredient, User
from Recipe.forms import SearchForms

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# TODO à mettre dans les def qui utilise c'est model 
def get_recipe():
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    categories = Category.objects.all()
    glasses = Glass.objects.all()
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    context = {"latest_recipe": latest_recipe, "categories": categories, "ingredients": ingredients, "glasses": glasses, "users": users}
    return context

def random(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    print('🚀 ~ file: views.py ~ line 7 ~ response', response);
    parsedResponse = formatRecipe(response['drinks'][0])
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    context = {'latest_recipe': latest_recipe, 'response': parsedResponse}
    return render(request, 'recipe-detail.html', context)

def formatRecipe(recipe):
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        measure = recipe['strMeasure' + str(i)]
        if ((ing is not None and measure is not None) and (ing != '' and measure != '')):
            recipeIngredients.append(ing + ' : ' + measure)
            
    return { 'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'], 'strDrinkThumb': recipe['strDrinkThumb'] }

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

def recipeDetail(request, id):
    try:
        recipe = Recipe.objects.get(pk=id)
        latest_recipe = Recipe.objects.order_by('created_at')[:4]
        categories = Category.objects.all()
        glasses = Glass.objects.all()
        users = User.objects.all()
        ingredients = Ingredient.objects.all()
        context = {'recipe': recipe, "latest_recipe": latest_recipe, "categories": categories, "ingredients": ingredients, "glasses": glasses, "users": users}

    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipe-detail.html', context)