from django.contrib import admin
from stock.models import StockProduct
# Register your models here.
#
@admin.register(StockProduct)#<--- esto le dice a Django que debe proporcionar una interfaz de administración para el modelo stock_product
class StockProduct (admin.ModelAdmin):
    pass
