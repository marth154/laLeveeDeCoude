from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    is_alcoholic = models.BooleanField(default=True)


# CF GROUP
# class Ingredient_Group(models.Model): 
#     recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.ManyToManyField(Ingredient, through='Recipe' )
#     quantity = models.CharField(max_length=250)