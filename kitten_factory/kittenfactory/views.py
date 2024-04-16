from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from .models import Product, Employee, Customer, Order, CustomerReturn, RawMaterial, SalesReport
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, OrderSerializer 
from .serializers import CustomerReturnSerializer, RawMaterialSerializer
from .serializers import SalesReportSerializer
from django.http import HttpResponse
from .forms import CustomerReturnForm, OrderForm, PaymentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy, reverse



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
    
    






class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
def product_list(request):
    response = requests.get('http://127.0.0.1:8000/kittenfactory/api/products/')  # Update with the actual API URL
    products = response.json() if response.status_code == 200 else []
    return render(request, 'product_list.html', {'products': products})


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





@method_decorator(login_required, name='dispatch')
class OrderHistoryView(ListView):
    model = Order
    template_name = 'order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Order.objects.filter(customer=customer)
        # Adjust the query to match how you identify orders (e.g., by user

def order_product_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            try:
                customer_profile = Customer.objects.get(user=request.user)
                order.customer = customer_profile
                order.save()
                return redirect('order_history')
            except Customer.DoesNotExist:
                # Handle the case where the user does not have a customer profile
                # Possible response: redirect to a profile creation page, or display an error
                return render(request, 'error.html', {'message': 'No customer profile found.'})
            
              # Redirect to the order history page or a confirmation page
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})
class OrderUpdateDeleteView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'delete_order.html'
    success_url = reverse_lazy('order_history')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'delete' in request.POST:
            self.object.delete()
            return redirect('order_history')
        else:  # Handle update
            response = super().post(request, *args, **kwargs)
            if self.form_valid(self.get_form()):
                return redirect('order_history')
            else:
                return response

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
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


class PaymentAdd(View):
    def get(self, request):
        form = PaymentForm()
        return render(request, 'payment/payment_add.html', {'form': form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        return render(request, 'payment/payment_add.html', {'form': form})
