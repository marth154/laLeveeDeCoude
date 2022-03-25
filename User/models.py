from django.db import models
from django.contrib.auth.models import User
from Recipe.models import Recipe

# Create your models here.


class User(models.Model):
    username = User.username
    password = User.password
    email = User.email
    is_admin = User.is_staff


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
