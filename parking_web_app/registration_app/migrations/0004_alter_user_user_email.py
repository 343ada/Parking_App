# Generated by Django 5.0.3 on 2024-05-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration_app", "0003_alter_user_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_email",
            field=models.EmailField(default="sombody@email.com", max_length=254),
        ),
    ]