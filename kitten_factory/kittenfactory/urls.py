from django.urls import path
from . import views
from .views import Home, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, EmployeeListCreateAPIView, Home
from .views import EmployeeRetrieveUpdateDestroyAPIView, CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView 
from .views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, ReturnListCreateAPIView, ReturnRetrieveUpdateDestroyAPIView
from .views import RawMaterialListCreateAPIView, RawMaterialRetrieveUpdateDestroyAPIView, PaymentCreateAPIView, make_payment
from .views import SalesReportListCreateAPIView, SalesReportRetrieveUpdateDestroyAPIView, submit_customer_return
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('employee/', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('customer/', CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('customer/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path('order/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
    path('return/', ReturnListCreateAPIView.as_view(), name='return-list'),
    path('return/<int:pk>', ReturnRetrieveUpdateDestroyAPIView.as_view(), name='return-detail'),
    path('rawmaterial/', RawMaterialListCreateAPIView.as_view(), name='rawmaterial-list'),
    path('rawmaterial/<int:pk>', RawMaterialRetrieveUpdateDestroyAPIView.as_view(), name='rawmaterial-detail'),
    path('report/', SalesReportListCreateAPIView.as_view(), name='report-list'),
    path('report/<int:pk>', SalesReportRetrieveUpdateDestroyAPIView.as_view(), name='report-details'),
    path('about/', views.Home.about_view, name='about'),
    path('contact/', views.Home.contact_view, name='contact'),
    path('signup/',  views.Home.signup_view, name='signup'),
    path('login/', views.Home.login_view, name='login'),
    path('products/', views.Product_List.as_view(), name='product-list'),
    path('contact/submit/', Home.contact_submit, name='contact-submit'),
    path('submit_return/', submit_customer_return, name='submit-return'),
    path ('view_payments/', PaymentCreateAPIView.as_view(), name="view-payments"),
    path('make_payment/', make_payment, name='make-payment'),
]
    



