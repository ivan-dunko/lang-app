# Generated by Django 4.2 on 2023-04-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lang_app", "0004_rename_difficulty_lesson_grade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ankicard",
            name="image",
            field=models.ImageField(upload_to="static/anki"),
        ),
    ]