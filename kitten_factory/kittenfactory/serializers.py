# serializers.py
from rest_framework import serializers
from .models import Product
from .models import Customer
from .models import Employee
from .models import RawMaterial
from .models import Order
from .models import CustomerReturn
from .models import SalesReport


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReturn
        fields = '__all__'




class SalesReportSerializer(serializers.ModelSerializer):
    most_popular_product = serializers.SerializerMethodField()
    least_popular_product = serializers.SerializerMethodField()

    def get_most_popular_product(self, obj):
        return obj.most_popular_product().name if obj.most_popular_product() else None
    def get_least_popular_product(self, obj):
        return obj.least_popular_product().name if obj.least_popular_product() else None
    
    class Meta:
        model = SalesReport
        fields = ['id', 'start_date', 'end_date', 'most_popular_product', 'least_popular_product']