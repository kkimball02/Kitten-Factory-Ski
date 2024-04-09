from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from django.urls import reverse, reverse_lazy
from .models import Product
from .serializers import ProductSerializer
class Login(View):

    template_name ='login.html'

    def get(self, request):

        return render(request, self.template_name,)
    
class Home(View):

    template_name ='home.html'

    def get(self, request):

        return render(request, self.template_name,)
    

# List and Create
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update and Delete
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer