from django.db import models
from User.models import User
from Ingredient.models import Ingredient

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)


class Glass(models.Model):
    name = models.CharField(max_length=250)


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_shared = models.BooleanField
    alcoholic = models.BooleanField
    glass_id = models.ForeignKey(Glass, on_delete=models.CASCADE)
    steps = models.CharField(max_length=500)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')


class Recipe_Ingredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=250)
