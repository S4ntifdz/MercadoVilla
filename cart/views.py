from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Cart, CartItem
from stock.models import StockProduct
from django.http import HttpResponse

class CartView(View):
    def get(self, request):
        
        cart, _ = Cart.objects.get_or_create(user=request.user)
        
        context = {
            'cart': cart,
        }
        return render(request, "cart.html", context)
    def clear_cart(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.cartitem_set.all().delete()
        return redirect('cart')
    
    def post(self, request): 
        if 'clear_cart' in request.POST:
            return self.clear_cart(request)

        product_id = int(request.POST.get('id'))
        quantity = int(request.POST.get('qt', 1))
        product = StockProduct.objects.get(pk=product_id)
        if product.quantity_stock >= quantity:
            product.quantity_stock -= quantity
            product.save()
        else:
            messages.error(request, 'No hay suficiente stock disponible para este producto.')
            return redirect('/publication/'+str(product_id)) 

        product = StockProduct.objects.get(pk=product_id) 
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        cart.update_cart_total()
        cart.save()
        return redirect('cart') 
    

#TODO falta validar stock

