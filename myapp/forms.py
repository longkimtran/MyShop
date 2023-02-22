from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Features


#Add Product

class AddProduct(ModelForm):
    class Meta:
        
        model = Features 
        fields = ['name', 'price', 'feature_image']

        label = {

            'name': '',
            'price': '',
            'feature_image': '',
        }

        wights = {

            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'price':forms.TextInput(attrs={'class': 'form-control',}),

        }





