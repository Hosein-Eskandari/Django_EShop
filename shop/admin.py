from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models


# Register your models here.
#admin.site.register(models.Product)
# admin.site.register(models.Category)
#admin.site.register(models.Cart)
#admin.site.register(models.Order)
#admin.site.register(models.OrderProduct)
admin.site.register(models.PaymentLog)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for category in queryset:
            category.delete()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'quantity', 'status', 'created_at']
    search_fields = ['title']
    list_filter = ['status']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for product in queryset:
            product.delete()


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'user', 'created_at']
    #search_fields = ['user']

    def delete_queryset(selfself, request : HttpRequest, queryset: QuerySet):
        for cart in queryset:
            cart.delete()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'user', 'status', 'created_at']
    #search_fields = ['user']
    list_filter = ['status']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for order in queryset:
            order.delete()


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'quantity', 'price', 'created_at', 'updated_at']
    sortable_by = ['updated_at']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for order_product in queryset:
            order_product.delete()




admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderProduct, OrderProductAdmin)

