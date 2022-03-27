from django.shortcuts import render
import requests
from Migration.tasks import add, tprint
from Recipe.models import Glass, Category, Recipe
from django.contrib.auth.models import User
from Ingredient.models import Ingredient, Ingredient_Group
from django.contrib.auth.decorators import login_required
from datetime import datetime


from huey import crontab
from huey.contrib.djhuey import task, periodic_task, db_task

# Create your views here.


def import_glass():
    glasses = Glass.objects.all()
    glasses.delete()
    print("Drop Glasses")
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/list.php?g=list').json()
    for i in range(len(response['drinks'])):
        Glass.objects.create(name=response['drinks'][i]['strGlass'], pk=i)
    print("Migration Glass done")


def import_recipe():
    # Creating a table to loop through all the letters of the alphabet and numbers
    loop = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    recipes = Recipe.objects.filter(is_migrate=True)
    if(recipes):
        recipes.delete()
        print("Drop Recipe")
    for i in loop:
        response = requests.get(
            "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + str(i)).json()
        if(response['drinks']):
            for k in range(len(response['drinks'])):
                if(response['drinks'][k]['strAlcoholic'] == 'Alcoholic'):
                    is_alcohol = True
                else:
                    is_alcohol = False
                glasses = Glass.objects.filter(
                    name=response['drinks'][k]['strGlass'])
                
                for glass in glasses:
                    glass_recipe = glass
                try:
                    category_recipe = Category.objects.get(
                        name=response['drinks'][k]['strCategory'])
                except:
                    print("Error Category")
                    category_recipe = None

                user_recipe = User.objects.get(username="admin")

                new_recipe = Recipe.objects.create(
                    pk=response['drinks'][k]['idDrink'],
                    name=response['drinks'][k]['strDrink'],
                    user_id=user_recipe,
                    category_id=category_recipe,
                    is_shared=True,
                    is_alcoholic=is_alcohol,
                    is_migrate=True,
                    thumbnail=response['drinks'][k]["strDrinkThumb"],
                    glass_id=glass_recipe,
                    steps=response['drinks'][k]["strInstructions"],
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )

                for j in range(1, 15):
                    ing = response['drinks'][k]['strIngredient' + str(j)]
                    measure = response['drinks'][k]['strMeasure' + str(j)]
                    if(ing is not None and measure is not None):
                        ingredients = Ingredient.objects.filter(name=ing)   
                        for ingredient in ingredients:
                            Ingredient_Group.objects.create(recipe=new_recipe, ingredient=ingredient,quantity=measure)
                print('Add new recipe ' + new_recipe.name)
    print("Migration Recipe done")


def import_ingredients():
    ingredients = Ingredient.objects.all()
    ingredients.delete()
    print("Drop Ingredients")
    for i in range(650):
        response = requests.get(
            "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid=" + str(i)).json()
        if(response['ingredients']):
            if(response['ingredients'][0]['strAlcohol'] == 'Yes'):
                is_alcohol = True
            else:
                is_alcohol = False

            new_ingredient = Ingredient.objects.create(name=response['ingredients'][0]['strIngredient'],
                                      description=response['ingredients'][0]['strDescription'],
                                      is_alcoholic=is_alcohol,
                                      pk=i)
            print("Add new ingredient " + new_ingredient.name)
    print("Migration Ingredient done")


def import_category():
    categories = Category.objects.all()
    categories.delete()
    print("Drop Category")
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list').json()
    for i in range(len(response['drinks'])):
        Category.objects.create(
            name=response['drinks'][i]['strCategory'], pk=i)
    print("Migration Category done")


@login_required(login_url="/login")
def import_data(request):
    add(1, 2)
    return render(request, 'migration.html')


# @periodic_task(crontab(minute='*/5'))
# def migration():
#     import_glass()
#     import_category()
#     import_ingredients()
#     import_recipe()
