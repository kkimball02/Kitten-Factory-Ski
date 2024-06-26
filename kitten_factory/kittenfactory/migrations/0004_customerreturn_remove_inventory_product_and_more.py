# Generated by Django 5.0.2 on 2024-04-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittenfactory', '0003_salesreport_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='rawMaterial',
        ),
        migrations.RemoveField(
            model_name='return',
            name='order',
        ),
        migrations.RemoveField(
            model_name='return',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='rawMaterial',
        ),
        migrations.DeleteModel(
            name='CustomerReview',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.DeleteModel(
            name='Return',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
