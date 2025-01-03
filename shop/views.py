
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST

from . import models
from .models import Product
from decimal import Decimal
from .cart import Cart

def checkout(request):
    return render(request, "checkout.html")


def index(request):
    products = models.Product.objects.all()
    # print(products)
    return render(request, "index.html", context={"products": products})


def detail(request, id: int, title: str):
    # product_detail = models.Product.objects.get(id=id)
    # try:
    #     product_detail = models.Product.objects.get(id=id)
    #     context = {"product_detail": product_detail}
    # except models.Product.DoesNotExist:
    #     raise Http404("product does not exist")

    product_detail = get_object_or_404(models.Product, id=id)
    context = {"product_detail": product_detail}
    return render(request, "detail.html", context=context)


def store(request):
    category = request.GET.get('category')
    if category is not None:
        products = models.Product.objects.filter(category__title=category)
        return render(request, "store.html", {"products": products})

    products = models.Product.objects.all()
    return render(request, "store.html", {"products": products})

@require_POST
def add_to_cart(request):
    product_id = int(request.POST.get("product_id"))
    quantity = int(request.POST.get("quantity"))
    update = True if request.POST.get("update") == '1' else False

    product = get_object_or_404(models.Product, id=product_id)

    cart = Cart(request)
    cart.add_to_cart(product_id, str(product.price), int(quantity), update)

    return redirect(reverse("shop:cart_detail"))

def cart_detail(request):
    cart = Cart(request)
    if cart:
        product_ids = cart.product_ids
        products = models.Product.objects.filter(id__in=product_ids)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart:
            item['total_price'] = Decimal(item['price']) * item['quantity']

        return render(request, "cart_detail.html", {"cart": cart})

    return render(request, "cart_detail.html")

def remove_from_cart(request, product_id):
    if Product.objects.filter(id=product_id).exists():
        cart = Cart(request)
        cart.remove_from_cart(str(product_id))
        return redirect(reverse("shop:cart_detail"))

    raise Http404("product doesnt exist.")