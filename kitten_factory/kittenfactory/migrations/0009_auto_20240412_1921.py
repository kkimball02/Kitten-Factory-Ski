# Generated by Django 5.0.2 on 2024-04-13 01:21

from django.db import migrations

def create_customer_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Customer = apps.get_model('kittenfactory', 'Customer')
    for user in User.objects.all():
        Customer.objects.create(user=user)
class Migration(migrations.Migration):

    dependencies = [
        ('kittenfactory', '0008_customer_user_employee_user'),
    ]

    operations = [ migrations.RunPython(create_customer_profiles),
    ]
