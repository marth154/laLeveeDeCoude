from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(max_length=50)
    type = models.BooleanField
