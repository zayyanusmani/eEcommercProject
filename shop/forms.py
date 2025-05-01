from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CartItem, Order

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
