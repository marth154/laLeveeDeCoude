from django.contrib import admin

from .models import Category
from .models import Glass
from .models import Recipe
from .models import Ingredient_Group

# Register your models here.
admin.site.register(Category)
admin.site.register(Glass)
admin.site.register(Recipe)
admin.site.register(Ingredient_Group)
