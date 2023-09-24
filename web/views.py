from django.shortcuts import render
from django.views import View
from stock.models import StockProduct

class ProductView(View):
    
    def get(self, request):  
        products = StockProduct.objects.all()
        return render(request, "home.html", {"products": products})
    
    def post(self, request):
        pass