from django.urls import path
from .views import index, detail, store, checkout, add_to_cart, cart_detail, remove_from_cart

app_name = 'shop'

urlpatterns = [
    path("", index, name="index"),
    path("store", store, name="store"),
    path("checkout/", checkout, name="checkout"),
    path("<int:id>/<str:title>/", detail, name="detail"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("cart/", cart_detail, name="cart_detail"),
    path("cart/remove/<int:product_id>", remove_from_cart, name="remove_from_cart"),
]
