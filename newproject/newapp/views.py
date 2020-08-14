from django.shortcuts import render
from django.http import  HttpResponse
from .models import Catogery,Products
from . forms import ProductForm,catogeryForm





def main_page(request):
    
    if request.method == 'POST':
        form1 = ProductForm(request.POST,request.FILES)
        form2 = catogeryForm(request.POST, request.FILES)
       
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
    else:
        form1 = ProductForm()
        form2 = catogeryForm()
    category = Catogery.objects.all()
    products = Products.objects.all()
    context = {
        'form1' : form1,
        'form2' : form2,
        'category' : category,
        'products' : products
    }
    return render(request,'newapp/home.html',context)