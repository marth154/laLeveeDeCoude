# Generated by Django 3.2.12 on 2022-03-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='alcoholic',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]
