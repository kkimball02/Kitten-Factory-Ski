from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics, viewsets
from .models import Product, Employee, Customer, Order, CustomerReturn, RawMaterial, SalesReport
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, OrderSerializer 
from .serializers import CustomerReturnSerializer, RawMaterialSerializer
from .serializers import SalesReportSerializer
from django.http import HttpResponse
from .forms import CustomerReturnForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a homepage or dashboard
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

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
    permission_classes = [IsAuthenticated]


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
@login_required
def order_history_view(request):
    # Fetch orders for the logged-in user
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer).order_by('-date')
    return render(request, 'order_history.html', {'orders': orders})

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
class ReturnListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerReturn.objects.all()
    serializer_class = CustomerReturnSerializer
    permission_classes = [IsAuthenticated]
@login_required
def submit_customer_return(request):
    if request.method == 'POST':
        form = CustomerReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CustomerReturnForm()
    return render(request, 'returns.html', {'form': form})  
    


class ReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerReturn.objects.all()
    serializer_class = CustomerReturnSerializer
    permission_classes = [IsAuthenticated]

class RawMaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [IsAuthenticated]

class RawMaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [IsAuthenticated]

class SalesReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    permission_classes = [IsAuthenticated]

class SalesReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = SalesReport.objects.all()
     serializer_class = SalesReportSerializer
     permission_classes = [IsAuthenticated]