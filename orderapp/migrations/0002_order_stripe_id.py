# Generated by Django 4.1.10 on 2023-08-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orderapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
