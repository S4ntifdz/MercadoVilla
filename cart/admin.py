from django.contrib import admin
from .models import CartModel

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    pass
