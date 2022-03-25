from django.shortcuts import render
from urllib3.util import Retry
import requests
from requests.adapters import HTTPAdapter
from django.http import Http404
from Recipe.models import Recipe, Category, Glass, User
from Recipe.forms import SearchForms
from Ingredient.models import Ingredient, Ingredient_Group

from operator import concat

import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from Recipe.forms import SearchForms
from User.models import Favorite


# TODO à mettre dans les def qui utilise c'est model
def get_recipe():
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    categories = Category.objects.all()
    glasses = Glass.objects.all()
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    context = {"latest_recipe": latest_recipe, "categories": categories,
               "ingredients": ingredients, "glasses": glasses, "users": users}
    return context


def random(request):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    parsedResponse = formatRecipe(request,response['drinks'][0])
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    context = {'latest_recipe': latest_recipe, 'response': parsedResponse}
    return render(request, 'recipe-detail.html', context)


def formatRecipe(request, recipe):
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        measure = recipe['strMeasure' + str(i)]
        if ((ing is not None and measure is not None) and (ing != '' and measure != '')):
            recipeIngredients.append(ing + ' : ' + measure)
    print(checked_favorite(request.user, recipe['idDrink']))
    return {'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'], 'strDrinkThumb': recipe['strDrinkThumb'], 'is_favorite': checked_favorite(request.user, recipe['idDrink'])}


def getId(n):
    return n.idDrink


def list(request):
    form = SearchForms()
    
    if(request.POST.get('remove')):
        change_favorite(request.POST, request.user, request.POST.get('remove'))
    elif(request.POST.get('add')):
        change_favorite(request.POST, request.user, request.POST.get('add'))
    

    if request.method == "POST":
        if request.POST.get("name"):
            query = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + \
                request.POST.get("name")
            response = requests.get(query)
            parsed = response.json()

            if parsed['drinks'] is not None:
                finalList = []
                for i in range(len(parsed['drinks'])):
                    finalList.append(formatRecipe(request,parsed['drinks'][i]))
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
                    responseDrink = requests.get(
                        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()
                    finalList.append(formatRecipe(request,responseDrink['drinks'][0]))
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
                    responseDrink = requests.get(
                        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()
                    finalList.append(formatRecipe(request,responseDrink['drinks'][0]))
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
                    responseDrink = requests.get(
                        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drinksIds[i]).json()
                    finalList.append(formatRecipe(request,responseDrink['drinks'][0]))
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
                finalList.append(formatRecipe(request,parsed['drinks'][i]))
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
            finalList.append(formatRecipe(request,parsed['drinks'][i]))

        paginator = Paginator(finalList, 10)
        page = request.GET.get('page', 1)
        try:
            paginateList = paginator.page(page)
        except PageNotAnInteger:
            paginateList = paginator.page(1)
        except EmptyPage:
            paginateList = paginator.page(paginator.num_pages)

        context = {
            'form': form,
            'recipes': paginateList,
        }

    return render(request, 'recipe-list.html', context)


def recipeDetail(request, id):
    if(request.method == 'POST'):
        change_favorite(request.POST, request.user, id)
    try:
        recipe = Recipe.objects.get(pk=id)
        latest_recipe = Recipe.objects.order_by('created_at')[:4]
        categories = Category.objects.all()
        glasses = Glass.objects.all()
        users = User.objects.all()
        ingredients = Ingredient_Group.objects.filter(recipe=recipe)
        is_favorite = Favorite.objects.filter(user=request.user, recipe=recipe)
        context = {'recipe': recipe, "latest_recipe": latest_recipe, "categories": categories,
                   "ingredients": ingredients, "glasses": glasses, "users": users, 'is_favorite': is_favorite}

    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipe-detail.html', context)


def change_favorite(post, username, recipre_id):
    if(post.get('remove')):
        recipe = Recipe.objects.get(pk=recipre_id)
        user = User.objects.get(username=username)
        Favorite.objects.filter(user=user, recipe=recipe).delete()
    elif(post.get('add')):
        recipe = Recipe.objects.get(pk=recipre_id)
        user = User.objects.get(username=username)
        Favorite.objects.create(user=user,recipe=recipe)
        
def checked_favorite(user, recipe):
    try:
        fav = Favorite.objects.get(user=user,recipe=recipe)
        if(fav is not None):
            return True
        else: 
            return False
    except:
        return None