from django.urls import path
from . import views
from .views import Home, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, EmployeeListCreateAPIView, Home
from .views import EmployeeRetrieveUpdateDestroyAPIView, CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView 
from .views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, ReturnListCreateAPIView, ReturnRetrieveUpdateDestroyAPIView
from .views import RawMaterialListCreateAPIView, RawMaterialRetrieveUpdateDestroyAPIView, InventoryListCreateAPIView, InventoryRetrieveUpdateDestroyAPIView
from .views import SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView, CustomerReviewListCreateAPIView, CustomerReviewRetrieveUpdateDestroyAPIView
from .views import SalesReportListCreateAPIView, SalesReportRetrieveUpdateDestroyAPIView
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
    path('inventory/', InventoryListCreateAPIView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryRetrieveUpdateDestroyAPIView.as_view(), name='inventory-detail'),
    path('supplier/', SupplierListCreateAPIView.as_view(), name='supplier-list'),
    path('supplier/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail'),
    path('review/', CustomerReviewListCreateAPIView.as_view(), name='review-list'),
    path('review/<int:pk>/', CustomerReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
    path('report/', SalesReportListCreateAPIView.as_view(), name='report-list'),
    path('report/<int:pk>', SalesReportRetrieveUpdateDestroyAPIView.as_view(), name='report-details'),
    path('about/', views.Home.about_view, name='about'),
    path('contact/', views.Home.contact_view, name='contact'),
    path('signup/',  views.Home.signup_view, name='signup'),
    path('login/', views.Home.login_view, name='login'),
    path('products/', views.Product_List.as_view(), name='product_list'),
    path('contact/submit/', Home.contact_submit, name='contact_submit'),
]
    



