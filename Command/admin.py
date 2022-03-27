from django.contrib import admin
from .models import Command
from .models import Command_Ingredients

# Register your models here.
admin.site.register(Command)
admin.site.register(Command_Ingredients)