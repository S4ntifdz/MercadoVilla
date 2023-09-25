from django.shortcuts import render
from django.views import View
from stock.models import StockProduct
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    
    def get(self, request): 
        template = loader.get_template("products.html") 
        user = request.user
        varios = StockProduct.objects.all()
        
        if user.is_anonymous:
            products = varios
        else:
            products = StockProduct.objects.filter(business_line=request.user.business_line_interes) 
        
        
        context = {
            "products": products,
            "varios": varios,
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass


#views.py ya eliminado:
# from django.shortcuts import render
# from django.views import View
# from stock.models import StockProduct

# class ProductView(View):
    
#     def get(self, request):  
#         products = StockProduct.objects.all()
#         return render(request, "products.html", {"products": products})
    
#     def post(self, request):
#         pass