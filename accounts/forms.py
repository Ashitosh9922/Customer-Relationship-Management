from django.forms import ModelForm
from .models import Customer, Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']  # Adjust fields according to your Customer model



