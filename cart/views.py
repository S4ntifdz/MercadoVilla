from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.template import loader
from .models import Cart, CartItem
from stock.models import StockProduct
from web.forms.checkout_form import CheckoutForm

class CartView(View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("cart.html")
        super().__init__(**kwargs)
        
    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        context = {
            'cart': cart,
        }
        
        if request.GET.get("route")== "checkout":
            self.template = loader.get_template("checkout.html")
            context["form"] =  CheckoutForm #punto de teoria, como pasar un formulario como contexto

        return render(request, self.template.template.name, context)

    def clear_cart(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.cartitem_set.all().delete()
        cart.update_cart_total() 
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
            return redirect('/publication/' + str(product_id))

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Actualizar la cantidad si ya existe el producto en el carrito
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        cart.update_cart_total()  # Actualizar el total del carrito
        return redirect('cart')
    
#SUMA EL PRECIO GENERAL, SIN EMBARGO CUANDO AGREGO EL 4 UNIDADES SOLO TERMINA AGREGANDO 1 