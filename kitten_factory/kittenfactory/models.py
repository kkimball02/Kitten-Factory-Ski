from django.db import models
from django.db.models import Max, Min

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

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rawMaterial = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    inventoryCount = models.IntegerField()

class Supplier(models.Model):
    rawMaterial = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=75)

class CustomerReview(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2)
    date = models.DateField(auto_now_add=True)

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expirationDate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25)

class SalesReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_orders = models.PositiveIntegerField()
    number_of_products_sold = models.PositiveIntegerField()
    def most_popular_product(self):
            return Product.objects.filter(order__date__range=(self.start_date, self.end_date)).annotate(
                max_sold=Max('quantity_sold')).order_by('-max_sold').first()
    def least_popular_product(self):
            return Product.objects.filter(order__date__range=(self.start_date, self.end_date)).annotate(
                min_sold=Min('quantity_sold')).order_by('min_sold').first()





