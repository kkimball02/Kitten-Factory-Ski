# forms.py

from django import forms
from .models import CustomerReturn, Order, Product, Payment

class CustomerReturnForm(forms.ModelForm):
    class Meta:
        model = CustomerReturn
        fields = ['customer_name', 'product_name', 'reason']

class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True)
    quantity = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Order
        fields = ['product', 'quantity', 'price']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
