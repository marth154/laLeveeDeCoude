# Generated by Django 3.2.12 on 2022-03-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ingredient', '0004_ingredient_is_alcoholic'),
        ('Recipe', '0003_alter_recipe_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient_group',
            field=models.ManyToManyField(to='Ingredient.Ingredient'),
        ),
        migrations.DeleteModel(
            name='Recipe_Ingredients',
        ),
    ]