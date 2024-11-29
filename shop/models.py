from tkinter.constants import CASCADE

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    deleted = models.BooleanField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    title = models.CharField(max_length=100)


class Product(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    image = models.ImageField()
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(BaseModel):
    total_price = models.DecimalField(decimal_places=2, max_digits= 10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.BooleanField(null=True)


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits= 10)


class PaymentLog(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits= 10)
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    status = models.CharField(max_length=100)
    error_code = models.CharField(max_length=200)

