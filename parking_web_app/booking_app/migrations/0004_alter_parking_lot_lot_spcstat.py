# Generated by Django 5.0.3 on 2024-05-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking_app", "0003_parking_lot_lot_totspace_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parking_lot",
            name="lot_spcstat",
            field=models.BooleanField(default=True),
        ),
    ]
