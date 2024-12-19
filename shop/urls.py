from django.urls import path
from .views import index, product, store, checkout



app_name = 'shop'

urlpatterns = [
    path("", index, name="index"),
    path("product/", product, name="product"),
    path("checkout/", checkout, name="checkout"),
    path("store/", store, name="store"),
]