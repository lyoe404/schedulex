# Generated by Django 5.2.1 on 2025-05-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
