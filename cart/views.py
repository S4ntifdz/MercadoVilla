from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import CartModel
from stock.models import StockProduct as StockModel


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        template = loader.get_template("cart.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        template = loader.get_template("cart.html")
        #validar que haya stock:
        
        #validar que no existe en el carro, y si existiera que sume 
        CartModel.objects.create(
            client=request.user,
            stock_id=request.POST.get("id"),
            qt = request.POST.get("qt")
        )
        #descontar el stock
        
        context = {}
        return HttpResponse(template.render(context, request))