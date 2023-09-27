from django.shortcuts import render
from django.views import View
from stock.models import StockProduct
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin    
from django.shortcuts import render, get_object_or_404

class PublicationView(LoginRequiredMixin, View):
    
    def get(self, request, product_id):
        # Buscar el producto por ID (puedes usar get_object_or_404 para manejar errores)
        publication_product = get_object_or_404(StockProduct, pk=StockProduct.code_product)
        
        template = loader.get_template('publication.html')
        context = {
            'publication_product': publication_product
        }
        return HttpResponse(template.render(context, request))
