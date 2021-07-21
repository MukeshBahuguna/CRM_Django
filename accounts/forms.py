from django.forms import ModelForm
from .models import Order,Customer
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields='__all__'
        exclude=['user']


class OrderForm(ModelForm):
    class Meta:
        model= Order #model name
        fields = '__all__' # all attributes/fields or to be specific['customer'] 

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        
        