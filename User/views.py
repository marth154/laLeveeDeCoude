from operator import ge
from reprlib import recursive_repr
from django.shortcuts import render

# from .models import User
from django.contrib.auth.models import User

from Ingredient.models import Ingredient_Group
from .models import Favorite
from .forms import RegisterForms, LoginForms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginCredentials(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get(
            "username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = LoginForms()
            context = {
                'form': form,
                'notExisting': "true"
            }
            return render(request, 'login.html', context)
    if request.method == 'GET':
        form = LoginForms()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


def registerCredentials(request):
    if request.method == 'POST':
        user = User.objects.filter(email__exact=request.POST.get("email"))
        if(user):
            form = RegisterForms()
            context = {
                'form': form,
                'existing': "true"
            }
            return render(request, 'register.html', context)
        else:
            user = User.objects.create_user(
                username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password"))
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = RegisterForms()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


@login_required(login_url="/login")
def bar(request):
    return render(request, 'bar.html')


@login_required(login_url="/login")
def favorites(request):
    recipes_with_ingredient = []
    try:
        my_favorites = Favorite.objects.filter(user_id=request.user)
    except:
        my_favorites = False
    for recipe in my_favorites:
        recipes_with_ingredient.append(get_ingredient(recipe.recipe))
        # recipes_with_ingredient.append(recipe.recipe)
    return render(request, 'my-favorite.html', {'my_favorites': recipes_with_ingredient})



def get_ingredient(recipe):
    list_ingredient = []
    array_recipe_ingredients = []
    ingredients = Ingredient_Group.objects.filter(recipe=recipe)
    for ingredient in ingredients:
        list_ingredient.append(ingredient)
    print(array_recipe_ingredients)
    array_recipe_ingredients.extend([list_ingredient])
    array_recipe_ingredients.extend([recipe])
    return array_recipe_ingredients