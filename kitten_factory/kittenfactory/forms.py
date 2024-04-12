# forms.py

from django import forms
from .models import CustomerReturn

class CustomerReturnForm(forms.ModelForm):
    class Meta:
        model = CustomerReturn
        fields = ['customer_name', 'product_name', 'reason']

        