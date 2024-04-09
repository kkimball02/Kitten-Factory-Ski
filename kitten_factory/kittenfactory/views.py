from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from django.urls import reverse
from django import forms

class Login(View):

    template_name ='login.html'

    def get(self, request):

        return render(request, self.template_name,)
    
class Home(View):

    template_name ='home.html'

    def get(self, request):

        return render(request, self.template_name,)
