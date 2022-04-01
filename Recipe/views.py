from datetime import datetime
import requests
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from Home.views import get_ingredient
from Ingredient.models import Ingredient, Ingredient_Group
from User.models import Favorite
import random
from Recipe.forms import CreateRecipe, SearchForms
from Recipe.models import Category, Glass, Recipe, User


def get_recipe():
    latest_recipe = Recipe.objects.order_by('-created_at')[:4]
    categories = Category.objects.all()
    glasses = Glass.objects.all()
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    context = {"latest_recipe": latest_recipe, "categories": categories,
               "ingredients": ingredients, "glasses": glasses, "users": users}
    return context


def random(request):

    recipes_with_ingredient = []
    latest_recipe = Recipe.objects.order_by('-created_at')[:4]
    for recipe in latest_recipe:
        recipes_with_ingredient.append(get_ingredient(recipe))
    
    if(request.method == 'POST'):
        if(request.POST.get('remove')):
            change_favorite(request.POST, request.user,
                            request.POST.get('remove'))
            recipe = Recipe.objects.get(pk=request.POST.get('remove'))
        elif(request.POST.get('add')):
            change_favorite(request.POST, request.user,
                            request.POST.get('add'))
            recipe = Recipe.objects.get(pk=request.POST.get('add'))
        context = {'latest_recipe': recipes_with_ingredient, 'recipe': get_ingredient(
            recipe), "is_favorite": checked_favorite(request.user, recipe)}

    if(request.method == "GET"):
        recipe = Recipe.objects.order_by('?').first()
        context = {'latest_recipe': recipes_with_ingredient, 'recipe': get_ingredient(
            recipe), "is_favorite": checked_favorite(request.user, recipe)}

    return render(request, 'recipe-detail.html', context)


def format_recipe(request, recipe):
    recipeIngredients = []
    for i in range(1, 15):
        ing = recipe['strIngredient' + str(i)]
        measure = recipe['strMeasure' + str(i)]
        if ((ing is not None and measure is not None) and (ing != '' and measure != '')):
            recipeIngredients.append(ing + ' : ' + measure)
    return {'idDrink': recipe['idDrink'], 'strDrink': recipe['strDrink'], 'strIngredients': recipeIngredients, 'strCategory': recipe['strCategory'], 'strGlass': recipe['strGlass'], 'strInstructions': recipe['strInstructions'], 'strAlcoholic': recipe['strAlcoholic'], 'strDrinkThumb': recipe['strDrinkThumb'], 'is_favorite': checked_favorite(request.user, recipe['idDrink'])}


def get_id(n):
    return n.idDrink


def list(request):
    form = SearchForms()

    if(request.POST.get('remove')):
        change_favorite(request.POST, request.user, request.POST.get('remove'))
    elif(request.POST.get('add')):
        change_favorite(request.POST, request.user, request.POST.get('add'))

    if request.method == "POST":
        if request.POST.get("name"):
            recipe_name = request.POST.get("name")
            response = Recipe.objects.filter(
                name__icontains=recipe_name, is_shared=True)

            if response is not None:
                finalList = []
                for recipe in response:
                    finalList.append(recipe)

                paginateList = paginator(request, finalList)

                context = {
                    'form': form,
                    'recipes': finalList,
                }
            else:
                context = {
                    'form': form,
                }

        elif request.POST.get("categories"):
            category_id = request.POST.get("categories")
            response = Recipe.objects.filter(
                category_id_id=category_id, is_shared=True)

            if response is not None:
                finalList = []
                for recipe in response:
                    finalList.append(recipe)

                paginateList = paginator(request, finalList)

                context = {
                    'form': form,
                    'recipes': paginateList,
                }
            else:
                context = {
                    'form': form,
                }

        elif request.POST.get("glasses"):
            glass_id = request.POST.get("glasses")
            response = Recipe.objects.filter(
                glass_id_id=glass_id, is_shared=True)

            if response is not None:
                finalList = []
                for recipe in response:
                    finalList.append(recipe)

                paginateList = paginator(request, finalList)

                context = {
                    'form': form,
                    'recipes': paginateList,
                }
            else:
                context = {
                    'form': form,
                }

        elif request.POST.get("alcoholic"):
            is_alcoholic = request.POST.get("alcoholic")
            response = Recipe.objects.filter(
                is_alcoholic=is_alcoholic, is_shared=True)

            if response is not None:
                finalList = []
                for recipe in response:
                    finalList.append(recipe)

                paginateList = paginator(request, finalList)

                context = {
                    'form': form,
                    'recipes': paginateList,
                }
            else:
                context = {
                    'form': form,
                }

        else:
            response = Recipe.objects.filter(is_shared=True)
            finalList = []
            for recipe in response:
                finalList.append(recipe)

            paginateList = paginator(request, finalList)

            context = {
                'form': form,
                'recipes': paginateList,
            }

    else:
        response = Recipe.objects.filter(is_shared=True)
        finalList = []
        for recipe in response:
            finalList.append(recipe)

        paginateList = paginator(request, finalList)

        context = {
            'form': form,
            'recipes': paginateList,
        }

    return render(request, 'recipe-list.html', context)


def recipe_detail(request, id):
    if(request.method == 'POST'):
        change_favorite(request.POST, request.user, id)
    try:
        recipe = Recipe.objects.get(pk=id)
        latest_recipe = Recipe.objects.order_by('created_at')[:4]
        categories = Category.objects.all()
        glasses = Glass.objects.all()
        users = User.objects.all()
        ingredients = Ingredient_Group.objects.filter(recipe=recipe)
        if request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(
                user=request.user, recipe=recipe)
        else:
            is_favorite = None
        context = {'recipe': get_ingredient(recipe), "latest_recipe": latest_recipe, "categories": categories,
                   "ingredients": ingredients, "glasses": glasses, "users": users, 'is_favorite': is_favorite}

    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipe-detail.html', context)


def change_favorite(post, username, recipe_id):
    if(post.get('remove')):
        recipe = Recipe.objects.get(pk=recipe_id)
        user = User.objects.get(username=username)
        Favorite.objects.filter(user=user, recipe=recipe).delete()
    elif(post.get('add')):
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404("Recipe does not exist")
        user = User.objects.get(username=username)
        Favorite.objects.create(user=user, recipe=recipe)


def checked_favorite(user, recipe):
    try:
        fav = Favorite.objects.get(user=user, recipe=recipe)
        if(fav is not None):
            return True
        else:
            return False
    except:
        return None


def get_ingredient(recipe):
    list_ingredient = []
    array_recipe_ingredients = []
    ingredients = Ingredient_Group.objects.filter(recipe=recipe)
    for ingredient in ingredients:
        list_ingredient.append(ingredient)
    array_recipe_ingredients.extend([list_ingredient])
    array_recipe_ingredients.extend([recipe])
    return array_recipe_ingredients


def paginator(request, recipes_list):
    paginator = Paginator(recipes_list, 20)
    page = request.GET.get('page', 1)
    try:
        paginateList = paginator.page(page)
    except PageNotAnInteger:
        paginateList = paginator.page(1)
    except EmptyPage:
        paginateList = paginator.page(paginator.num_pages)

    return paginateList


def add(request):
    form = CreateRecipe()
    
    if(request.POST.get('remove')):
        change_favorite(request.POST, request.user, request.POST.get('remove'))
    elif(request.POST.get('add')):
        change_favorite(request.POST, request.user, request.POST.get('add'))

    if request.method == "POST":
        user = User.objects.get(username=request.user)
        category = Category.objects.get(pk=request.POST.get('categories'))
        glass = Glass.objects.get(pk=request.POST.get('glasses'))

        new_cocktail = Recipe.objects.create(
            name=request.POST.get('name'),
            user_id=user,
            category_id=category,
            thumbnail=None,
            is_shared=request.POST.get('is_shared'),
            is_migrate=False,
            is_alcoholic=request.POST.get('alcoholic'),
            glass_id=glass,
            steps=request.POST.get('steps'),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        for ingredient in request.POST.getlist("ingredients"):
            new_ingredient = Ingredient.objects.filter(pk=ingredient)
            for ing in new_ingredient:
                Ingredient_Group.objects.create(
                    recipe=new_cocktail, ingredient=ing, quantity="")
        # on prépare un nouveau message
        messages.success(request, 'New cocktail created successfully !')
        context = {'recipe': get_ingredient(new_cocktail)}

        return render(request, 'recipe-detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request, 'recipe-add.html', context)
