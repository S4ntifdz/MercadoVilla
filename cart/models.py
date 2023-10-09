
from django.db import models
from clients.models import ClientModel
from stock.models import StockProduct


class Cart(models.Model):
    user = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    total_quantity = models.PositiveIntegerField(default=0) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    def __str__(self):
        return f"Carrito de {self.user.username}"
    def update_cart_total(self):
        cart_items = self.cartitem_set.all()
        total_quantity = 0
        total_price = 0
        for item in cart_items:
            total_quantity += item.quantity
            total_price += item.total_price
        self.total_quantity = total_quantity
        self.total_price = total_price
        self.save()
    def clear_cart(self):
        self.cartitem_set.all().delete()
        self.update_cart_total()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  
    product = models.ForeignKey(StockProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name_product} en {self.cart}"
#actualizo el carro despues de aggregar un producto
    def save(self, *args, **kwargs):
        self.cart.update_cart_total()
        super().save(*args, **kwargs)
        
    @property
    def qt_items(self):
        return self.cart.cartitem_set.count()
