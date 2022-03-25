from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)


class Glass(models.Model):
    name = models.CharField(max_length=250)


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    thumbnail = models.CharField(max_length=250, null=True)
    is_shared = models.BooleanField(default=False)
    is_migrate = models.BooleanField(default=False)
    is_alcoholic = models.BooleanField(default=True)
    glass_id = models.ForeignKey(Glass, on_delete=models.CASCADE, null=True)
    steps = models.TextField(null=True)
    # ingredient_group = models.ManyToManyField(Ingredient)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')
