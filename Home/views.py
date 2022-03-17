from django.shortcuts import render
from Recipe.models import Category, Ingredient, Recipe, User

# Create your views here.


def home(request):
    if request.user:
        return render(request, 'home.html')
    else:
        print("User isn't authenticated")
        return render(request, 'home.html')
        
def latest_recipe_list(request):
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    categories = Category.objects.all()
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    
    context = { "latest_recipe": latest_recipe, "categories": categories, "ingredients": ingredients, "users": users}
    return render(request, "last-recipe.html", context)
