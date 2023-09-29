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


        product_id = int(request.POST.get('id'))
        quantity = int(request.POST.get('qt', 3))  
        product = StockProduct.objects.get(pk=product_id) 
        
        cart, _ = Cart.objects.get_or_create(user=request.user) 
        # _ sirve para ignorar el segundo valor que retorna get_or_create, 
        # que es un booleano que indica si se creó o no el objeto

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        
        context ={
            'cart': cart,
            'cart_item': cart_item,
            'product': product,
            'quantity': quantity,
        }
        template = loader.get_template("cart.html")
        return HttpResponse(template.render(context, request))