from django.shortcuts import render
from django.views import View
from stock.models import StockProduct
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin


# class PublicationView(LoginRequiredMixin, View):
    
#     def get(self, request):
#         publication_product = StockProduct.objects.filter(publication=True) 
#         # aca tengo que lograr que se envie solo el producto que yo seleccione 
        
#         template = loader.get_template('publication.html')
#         context = {
#             'publication_product': publication_product
#         }
#         return HttpResponse(template.render(context, request))
    
from django.shortcuts import render, get_object_or_404

class PublicationView(LoginRequiredMixin, View):
    
    def get(self, request, code_product):
        publication_product = get_object_or_404(StockProduct, code_product=code_product, publication=True)
        template = loader.get_template('publication.html')
        context = {
            'publication_product': publication_product
        }
        return HttpResponse(template.render(context, request))
