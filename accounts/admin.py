from django.contrib import admin
from . import models
from django.http import HttpRequest
from django.db.models.query import QuerySet
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined']
    search_fields = ['username']

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet):
        for user in queryset:
            user.delete()

admin.site.register(models.User, UserAdmin)



