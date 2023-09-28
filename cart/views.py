from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.models import StockProduct as StockModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Cart, CartItem
from stock.models import StockProduct
from django.http import HttpResponse

class CartView(View):
    def get(self, request):
        template = loader.get_template("cart.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'Debes iniciar sesión para agregar elementos al carrito.')
            return redirect('login')  


        product_id = request.POST.get('id')
        quantity = int(request.POST.get('qt', 1))  

        try:
            product = StockProduct.objects.get(pk=product_id)
        except StockProduct.DoesNotExist:
            messages.error(request, 'El producto seleccionado no existe.')
            return redirect('home')  # Redirige a la página de inicio o a donde desees

        
        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        messages.success(request, f'Se ha agregado "{product.name_product}" al carrito.')

        return redirect('cart')  # Redirige al carrito después de agregar el producto
