from django.db import models
from django.db.models import Max, Min
from django.contrib.auth.models import User

# Create your models here.
# models.py


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    makeup = models.CharField(max_length = 50)
    size = models.IntegerField()

    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee', null=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=75)
    position = models.CharField(max_length= 75)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', null=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=75, null=True)

    def __str__(self):
        return self.user.username

class RawMaterial(models.Model):
    type = models.CharField(max_length=50)
    quantityOnHand = models.IntegerField()
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank= True, default=True)
    quantity = models.IntegerField(blank=True, default=True)
    date = models.DateField(blank=True, default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

class CustomerReturn(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    reason = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.product_name}"


    
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





