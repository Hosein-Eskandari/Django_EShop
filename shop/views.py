
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def checkout(request):
    return render(request, "checkout.html")

def index(request):
    return redirect(reverse("shop:store"))
    # return render(request, "index.html")
 
def product(request):
    return render(request, "product.html")

def store(request):
    return render(request, "store.html")


