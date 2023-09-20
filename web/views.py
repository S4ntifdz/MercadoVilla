from django.shortcuts import render
from django.views import View
from stock.models import StockProduct

class ProductView(View):
    def get(self, request):  # Debes usar el método "get" para las solicitudes GET
        products = StockProduct.objects.all()
        return render(request, "home.html", {"products": products})
