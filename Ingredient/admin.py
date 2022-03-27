from django.contrib import admin
from .models import Ingredient
from .models import Ingredient_Group

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Ingredient_Group)
