from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    username = User.username
    password = User.password
    email = User.email
    role = User.is_staff


class Category(models.Model):
    name = models.CharField(max_length=250)


class Glass(models.Model):
    name = models.CharField(max_length=250)


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(max_length=50)
    type = models.CharField(max_length=250)


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    shared = models.BooleanField
    alcoholic = models.BooleanField
    glass_id = models.ForeignKey(Glass, on_delete=models.CASCADE)
    createdAt = models.DateTimeField('created at')
    updatedAt = models.DateTimeField('updated at')


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Reciepes_Ingredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=250)


class Command(models.Model):
    amount = models.IntegerField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField('created at')
    isPayed = models.BooleanField


class Commands_Ingredients(models.Model):
    command_id = models.ForeignKey(Command, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=50)
