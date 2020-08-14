from django import forms
from django.forms import ModelForm
from .models import Products,Catogery

class ProductForm(ModelForm):
    image1= forms.ImageField(error_messages = {'invalid':("Image files only")}, widget=forms.FileInput, required=False)

    class Meta:
        model = Products
        fields = ('name','price','image1')

class catogeryForm(ModelForm):
    image= forms.ImageField(error_messages = {'invalid':("Image files only")}, widget=forms.FileInput, required=False)

    class Meta:
            model = Catogery
            fields = ('name','image')

    