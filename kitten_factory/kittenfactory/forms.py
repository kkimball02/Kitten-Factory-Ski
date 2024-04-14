# forms.py

from django import forms
from .models import CustomerReturn, Order, Product

class CustomerReturnForm(forms.ModelForm):
    class Meta:
        model = CustomerReturn
        fields = ['customer_name', 'product_name', 'reason']

class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True)
    quantity = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Order
        fields = ['product', 'quantity']

