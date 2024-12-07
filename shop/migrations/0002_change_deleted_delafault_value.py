# Generated by Django 5.1.3 on 2024-12-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_create_shop_entities"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="deleted",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="category",
            name="deleted",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="order",
            name="deleted",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="orderproduct",
            name="deleted",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="product",
            name="deleted",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
