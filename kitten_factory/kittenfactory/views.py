from django.shortcuts import render
from django.views import View
from rest_framework import generics
from .models import Product, Employee, Customer, Order, Return, RawMaterial
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, OrderSerializer, ReturnSerializer, RawMaterialSerializer

class Login(View):
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, self.template_name)

class Home(View):
    template_name = 'home.html'
    
    def get(self, request):
        
        return render(request, self.template_name,)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReturnListCreateAPIView(generics.ListCreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

class ReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

class RawMaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class RawMaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
