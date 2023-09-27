from django.shortcuts import render
from django.views import View
from stock.models import StockProduct
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin    
from django.shortcuts import render, get_object_or_404

class PublicationView(LoginRequiredMixin, View):
    
    def get(self, request, code_product):
        
        publication_product =  get_object_or_404(StockProduct, pk=code_product)
        code_product = publication_product.code_product
        template = loader.get_template('publication.html')
        context = {
            'publication_product': publication_product,
            'code_product' : code_product,
        }
        return HttpResponse(template.render(context, request))