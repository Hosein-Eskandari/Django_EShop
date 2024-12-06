from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models


# Register your models here.
admin.site.register(models.Product)
# admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderProduct)
admin.site.register(models.PaymentLog)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for category in queryset:
            category.delete()


admin.site.register(models.Category, CategoryAdmin)
