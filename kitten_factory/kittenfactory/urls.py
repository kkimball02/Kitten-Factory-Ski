from django.urls import path
from . import views
from .views import Home, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, EmployeeListCreateAPIView, Home
from .views import EmployeeRetrieveUpdateDestroyAPIView, CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView 
from .views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, ReturnListCreateAPIView, ReturnRetrieveUpdateDestroyAPIView
<<<<<<< HEAD
from .views import RawMaterialListCreateAPIView, RawMaterialRetrieveUpdateDestroyAPIView, product_list, delete_order
from .views import SalesReportListCreateAPIView, SalesReportRetrieveUpdateDestroyAPIView, submit_customer_return
=======
from .views import RawMaterialListCreateAPIView, RawMaterialRetrieveUpdateDestroyAPIView, product_list, order_detail_view
from .views import SalesReportListCreateAPIView, SalesReportRetrieveUpdateDestroyAPIView, submit_customer_return, OrderUpdateDeleteView
>>>>>>> 337d5fd9a61a73e0160f514376ea7aeb6f1adb5d
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product'),
    path('api/product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('api/employee/', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('api/employee/<int:pk>', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('api/customer/', CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('api/customer/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path('api/order/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('api/order/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
    path('api/return/', ReturnListCreateAPIView.as_view(), name='return-list'),
    path('api/return/<int:pk>', ReturnRetrieveUpdateDestroyAPIView.as_view(), name='return-detail'),
    path('api/rawmaterial/', RawMaterialListCreateAPIView.as_view(), name='rawmaterial-list'),
    path('api/rawmaterial/<int:pk>', RawMaterialRetrieveUpdateDestroyAPIView.as_view(), name='rawmaterial-detail'),
    path('api/report/', SalesReportListCreateAPIView.as_view(), name='report-list'),
    path('api/report/<int:pk>', SalesReportRetrieveUpdateDestroyAPIView.as_view(), name='report-details'),
    path('about/', views.Home.about_view, name='about'),
    path('contact/', views.Home.contact_view, name='contact'),
    path('contact/submit/', Home.contact_submit, name='contact-submit'),
    path('submit_return/', submit_customer_return, name='submit-return'),
    path('order_history/', views.order_history_view, name='order_history'),
    path('order-form/', views.order_product_view, name='order-form'),
    path('products/', product_list, name='product-list'),
<<<<<<< HEAD
    path('order/<int:order_id>/delete', delete_order, name='delete-order'),
    
    
=======
    path('order/<int:pk>/', order_detail_view, name='order-details'),
    path('order/<int:pk>/edit/', OrderUpdateDeleteView.as_view(), name='order-update-delete'),
>>>>>>> 337d5fd9a61a73e0160f514376ea7aeb6f1adb5d
]


    
    

    



