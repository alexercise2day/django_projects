# Generated by Django 4.1.5 on 2023-02-09 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cocktail_book", "0006_remove_gin_price_remove_rum_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vodka",
            name="image",
            field=models.ImageField(default="", upload_to="img/"),
        ),
    ]
