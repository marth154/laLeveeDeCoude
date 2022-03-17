from django.db import models
from User.models import User
from Ingredient.models import Ingredient

# Create your models here.


class Command(models.Model):
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('created at')


class Command_Ingredients(models.Model):
    command_id = models.ForeignKey(Command, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
