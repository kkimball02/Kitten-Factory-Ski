from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from .models import Product, Employee, Customer, Order, Return, RawMaterial, Inventory, Supplier, CustomerReview, SalesReport
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, OrderSerializer 
from .serializers import ReturnSerializer, RawMaterialSerializer, InventorySerializer, SupplierSerializer
from .serializers import CustomerReviewSerializer, SalesReportSerializer
from django.http import HttpResponse


class Home(View):
    template_name = 'home.html'
    
    def get(self, request):
        
        return render(request, self.template_name)
    

    def about_view(request):
        
        return render(request,'about.html')
    
    def contact_view(request):
        
        return render(request, 'contact.html')
    
    def contact_submit(request):
        if request.method == 'POST': #Check if the request method is POST.
        # Process your form data here
            name = request.POST.get('name') #If it is, retrieve the values of the 'name', 'email', and 'message' fields from the request's POST data.
            email = request.POST.get('email')
            message = request.POST.get('message')
            return HttpResponse("Thank you for your submission!")
        else:
            return HttpResponse("Invalid request", status=400)

    def signup_view(request):

        return render(request, 'signup.html')
    
    def login_view(request):

        return render(request, 'login.html')
    
    
class Product_List(View):
    
    template_name = 'product_list.html'
   
    def get(self, request):

        return render(request, self.template_name)


    
    


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

class InventoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CustomerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerReview.objects.all()
    serializer_class = SupplierSerializer

class CustomerReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class SalesReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

class SalesReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = SalesReport.objects.all()
     serializer_class = SalesReportSerializer