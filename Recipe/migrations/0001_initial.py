# Generated by Django 4.0.3 on 2022-03-11 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ingredient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('steps', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.category')),
                ('glass_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.glass')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=250)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ingredient.ingredient')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.recipe')),
            ],
        ),
    ]