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
    is_shared = models.BooleanField(default=False)
    alcoholic = models.BooleanField(default=True)
    glass_id = models.ForeignKey(Glass, on_delete=models.CASCADE)
    steps = models.TextField()
    ingredient_group = models.ManyToManyField(Ingredient)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')


