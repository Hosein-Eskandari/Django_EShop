
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST

from . import models


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

    product = get_object_or_404(models.Product, id=product_id)

    cart = request.session.get("cart")

    if not cart:
        cart = request.session["cart"] = {}

    cart[product_id] = {
        "quantity" : quantity,
        "price" : str(product.price)
    }

    request.session["cart"] = cart

    request.session.modified = True

    return redirect(reverse("shop:cart_detail"))


def cart_detail(request):
    cart = request.session.get("cart")
    product_ids = cart.keys()
    products = models.Product.objects.filter(id__in=product_ids)
    for product in products:
        cart[str(product.id)]["product"] = product
    if cart:
        return render(request, "cart_detail.html", {"cart": cart})

    return render(request, "cart_detail.html")

