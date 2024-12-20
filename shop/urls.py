from django.urls import path
from .views import index, detail, store, checkout



app_name = 'shop'

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/<str:title>/", detail, name="detail"),
    path("checkout/", checkout, name="checkout"),
    path("store", store, name="store"),
]