# Generated by Django 3.2.12 on 2022-03-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_auto_20220311_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.TextField(),
        ),
    ]