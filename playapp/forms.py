from django import forms
from .models import Order  # make sure your model is named Order, not order

class OnlineOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'address', 'quantity']
        
        

