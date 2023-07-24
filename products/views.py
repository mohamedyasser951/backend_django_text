from django.shortcuts import render

# Create your views here.

def products(request):
    return render("products/","products/products.html",)

def product(request):
    return render("product/","products/product.html",)