from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class SoftUserManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    deleted = models.BooleanField(default=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
