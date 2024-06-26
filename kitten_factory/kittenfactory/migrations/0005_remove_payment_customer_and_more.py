# Generated by Django 5.0.2 on 2024-04-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittenfactory', '0004_customerreturn_remove_inventory_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='expirationDate',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
