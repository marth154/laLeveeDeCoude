from django.shortcuts import render
from Recipe.models import Category, Recipe, User
from Ingredient.models import Ingredient_Group
from django.http import Http404
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url="/login")
def home(request):
    last_recipe_with_ingregients = []
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    for recipe in latest_recipe:
        last_recipe_with_ingregients.append(get_ingredient(recipe))
    print(last_recipe_with_ingregients)
    categories = Category.objects.all()
    users = User.objects.all()
    
    context = { "latest_recipe": last_recipe_with_ingregients, "categories": categories, "users": users}
    if request.user:
        return render(request, 'home.html', context)
    else:
        print("User isn't authenticated")
        return render(request, 'home.html')

def latest_recipe_list(request):
    return render(request, "last-recipe.html")


def get_ingredient(recipe):
    list_ingredient = []
    array_recipe_ingredients = []
    ingredients = Ingredient_Group.objects.filter(recipe=recipe)
    for ingredient in ingredients:
        list_ingredient.append(ingredient)
    array_recipe_ingredients.extend([list_ingredient])
    array_recipe_ingredients.extend([recipe])
    return array_recipe_ingredients