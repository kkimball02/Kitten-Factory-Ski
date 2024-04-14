# forms.py

from django import forms
<<<<<<< HEAD
from .models import CustomerReturn, Order, Product
=======
from .models import CustomerReturn, Order, Product, Payment
>>>>>>> 337d5fd9a61a73e0160f514376ea7aeb6f1adb5d

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

<<<<<<< HEAD
=======
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
>>>>>>> 337d5fd9a61a73e0160f514376ea7aeb6f1adb5d
