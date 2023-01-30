# Generated by Django 4.1.5 on 2023-01-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cocktail_book", "0004_vodka_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("ingredients", models.TextField(default="", max_length="1000")),
                ("instructions", models.TextField(default="", max_length="1000")),
            ],
        ),
        migrations.CreateModel(
            name="Tequila",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("ingredients", models.TextField(default="", max_length="1000")),
                ("instructions", models.TextField(default="", max_length="1000")),
            ],
        ),
        migrations.CreateModel(
            name="Whiskey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("ingredients", models.TextField(default="", max_length="1000")),
                ("instructions", models.TextField(default="", max_length="1000")),
            ],
        ),
        migrations.DeleteModel(name="cocktail",),
        migrations.RenameField(
            model_name="vodka", old_name="description", new_name="ingredients",
        ),
        migrations.AddField(
            model_name="rum",
            name="ingredients",
            field=models.TextField(default="", max_length="1000"),
        ),
        migrations.AddField(
            model_name="rum",
            name="instructions",
            field=models.TextField(default="", max_length="1000"),
        ),
        migrations.AddField(
            model_name="vodka",
            name="instructions",
            field=models.TextField(default="", max_length="1000"),
        ),
    ]
