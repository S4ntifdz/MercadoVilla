from django.db import models
from clients.models import ClientModel
from stock.models import StockProduct

class CartModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockProduct, on_delete=models.CASCADE)
    qt = models.PositiveIntegerField(default=1)













# from clients.models import ClientModel
# from stock.models import StockProduct

# class Cart(models.Model):
#     user = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(null=True)
#     def __str__(self):
#         return f"Carrito de {self.user.username}"

# class CartItem(models.Model):
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     product = models.ForeignKey(StockProduct, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     @property

#     def total_price(self): 
#         return self.quantity * self.product.price
    
#     def __str__(self):
#         return f"{self.quantity} x {self.product.name_product} en {self.cart}"

#     MI DUDA ES SI TENGO QUE CREAR UN MODELO "PADRE" QUE ACUMULE VARIOS 
#     MODELOS "HIJOS", LOS HIJOS ESTAN INTEGRADOS POR UN PRODUCTO, PRECIO Y CANTIDAD
#     Y EL MODELO PADRE SOLO SUMA LOS PRECIOS PARA UN PRECIO TOTAL DE COMPRA