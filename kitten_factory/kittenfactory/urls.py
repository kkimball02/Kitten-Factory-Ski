from django.contrib import admin
from django.urls import path, include
from .views import Login, Home, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
from . import views

urlpatterns = [
    path('login/', Login.as_view(), name ='login.html'),
    path('home/', Home.as_view(), name='home.html'),
    path('product/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]