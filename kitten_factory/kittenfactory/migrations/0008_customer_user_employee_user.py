# Generated by Django 5.0.2 on 2024-04-13 01:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittenfactory', '0007_remove_order_status_order_price_order_product_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
