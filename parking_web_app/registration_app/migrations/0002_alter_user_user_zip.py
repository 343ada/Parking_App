# Generated by Django 5.0.3 on 2024-05-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_zip",
            field=models.CharField(max_length=5),
        ),
    ]
