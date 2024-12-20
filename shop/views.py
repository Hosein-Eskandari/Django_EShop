
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import models


def checkout(request):
    return render(request, "checkout.html")

def index(request):
    products = models.Product.objects.all()
    print(products)
    return render(request, "index.html", context = {"products" : products})

def detail(request, id:int, title:str):
    # product_detail = models.Product.objects.get(id=id)
    # try:
    #     product_detail = models.Product.objects.get(id=id)
    #     context = {"product_detail": product_detail}
    # except models.Product.DoesNotExist:
    #     raise Http404("product does not exist")

    product_detail = get_object_or_404(models.Product, id=id)
    context = {"product_detail" : product_detail}
    return render(request, "detail.html", context = context)

def store(request):
    return render(request, "store.html")


