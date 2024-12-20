from audioop import reverse
from tkinter.constants import CASCADE
from typing import Any

from django.conf import settings
#from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q  # for or operation
from .utility import upload_file_with_date
# Create your models here.

class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted = False)
        # return super().get_queryset().filter(Q(deleted = False) | Q(deleted = None)) # or operation

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True



class Category(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    image = models.ImageField(upload_to=upload_file_with_date(base_dir="media_files", sub_dir="product_images"))
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True)

    def __str__(self) -> str:
        return self.title

    def get_fields(self):
        return [(field.name, getattr(self, field.name)) for field in self._meta.fields]

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})


class Cart(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    # def __str__(self) -> str:
    #     return self.user.__str__


class Order(BaseModel):
    total_price = models.DecimalField(decimal_places=2, max_digits= 10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

