from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics, viewsets
from .models import Product, Employee, Customer, Order, CustomerReturn, RawMaterial, SalesReport, Payment
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, OrderSerializer 
from .serializers import CustomerReturnSerializer, RawMaterialSerializer
from .serializers import SalesReportSerializer, PaymentSerializer
from django.http import HttpResponse
from .forms import CustomerReturnForm



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
    queryset = CustomerReturn.objects.all()
    serializer_class = CustomerReturnSerializer

def submit_customer_return(request):
    if request.method == 'POST':
        form = CustomerReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CustomerReturnForm()
    return render(request, 'returns.html', {'form': form})  
    
class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def make_payment(request):
    return render(request, 'make_payment.html')


class ReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerReturn.objects.all()
    serializer_class = CustomerReturnSerializer

class RawMaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class RawMaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer


class SalesReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

class SalesReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = SalesReport.objects.all()
     serializer_class = SalesReportSerializer