# Generated by Django 3.2.12 on 2022-03-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Command', '0002_auto_20220311_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='command_ingredients',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
