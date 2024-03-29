# Generated by Django 4.2.7 on 2023-11-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text="Enter the book's natural language (e.g. Swahili, Finnish, Japanese etc.)", max_length=200, unique=True),
        ),
    ]
