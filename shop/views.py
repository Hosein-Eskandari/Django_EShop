
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from . import models


def checkout(request):
    return render(request, "checkout.html")

def index(request):
    products = models.Product.objects.all()
    print(products)
    return render(request, "index.html", context = {"products" : products})

def product(request):
    return render(request, "product.html")

def store(request):
    return render(request, "store.html")


