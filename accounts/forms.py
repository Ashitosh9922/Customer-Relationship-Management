from django.forms import ModelForm
from .models import Customer, Order
from django import forms

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']  # Adjust fields according to your Customer model



