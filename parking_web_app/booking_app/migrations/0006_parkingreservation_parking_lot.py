# Generated by Django 5.0.3 on 2024-05-04 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking_app", "0005_alter_book_user_book_user_parkingreservation"),
    ]

    operations = [
        migrations.AddField(
            model_name="parkingreservation",
            name="parking_lot",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="booking_app.parking_lot",
            ),
        ),
    ]