from django.contrib import admin
from django.urls import path, include
from .views import Login,Home

urlpatterns = [
    path('login/', Login.as_view(), name ='login.html'),
    path('home/', Home.as_view(), name='home.html'),
]