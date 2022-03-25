from django.db import models
from Recipe.models import Recipe
from User.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=100000, null=True)
    # price = models.IntegerField()
    is_alcoholic = models.BooleanField(default=True)


class Ingredient_Group(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=250)
