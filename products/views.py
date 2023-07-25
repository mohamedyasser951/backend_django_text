from django.shortcuts import render
from .models import  product as pr
# Create your views here.

def products(request):
    return render(request,"products/products.html",{"pro":pr.objects.all()})

def product(request):
    return render(request,"products/product.html",)