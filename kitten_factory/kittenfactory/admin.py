from django.contrib import admin
from .models import Employee, Customer, Product, Order, CustomerReturn, RawMaterial, SalesReport

# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CustomerReturn)
admin.site.register(RawMaterial)
admin.site.register(SalesReport)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phoneNumber', 'position')
    search_fields = ('firstName', 'lastName', 'email')
    list_filter = ('position',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phoneNumber', 'address')
    search_fields = ('firstName', 'lastName', 'email')
    list_filter = ('address',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'makeup', 'size')
    search_fields = ('name', 'description', 'makeup')
    list_filter = ('makeup',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'date')
    search_fields = ('status',)
    list_filter = ('date', 'status')


class ReturnAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'reason')
    search_fields = ('reason',)
    list_filter = ('product',)


class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('type', 'quantityOnHand')
    search_fields = ('type',)
    list_filter = ('type',)



class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneNumber', 'address')
    search_fields = ('name', 'email')
    list_filter = ('name',)



class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'total_sales', 'number_of_orders', 'number_of_products_sold')
    list_filter = ('start_date', 'end_date')