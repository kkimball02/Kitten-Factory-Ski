from django.db import models

# Create your models here.
# models.py


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    makeup = models.CharField(max_length = 50)
    size = models.IntegerField()

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=75)
    position = models.CharField(max_length= 75)

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=75, blank=True, null=True)

class RawMaterial(models.Model):
    type = models.CharField(max_length=50)
    quantityOnHand = models.IntegerField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)

class Return(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reason = models.TextField()



