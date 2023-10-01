from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.models import StockProduct
#from comunication.models import ComunicationModel
from clients.models import ClientModel
from django.shortcuts import redirect
from django.urls import reverse
from comunication.models import ComunicationModel
from clients.models import ClientModel

class ComunicationView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("comunication.html")
        super().__init__(**kwargs)
    
    def get(self,request):
        stock = StockProduct.objects.get(pk=request.GET.get("item"))
        
        context = {
            "seller" : stock.user.pk,
            
            "initial_text" : f"Hola {stock.user.username}, me gustaria consultarle sobre el producto '{stock.name_product}' que vi en su tienda online. ",
        }
        return HttpResponse(self.template.render(context, request)) 
    def post(self,request):
        ComunicationModel.objects.create(
            client_question = ClientModel.objects.get(pk=int(request.POST.get("client"))),
            client_seller = ClientModel.objects.get(pk=int(request.POST.get("client_seller"))),
            question = request.POST.get("question"),
        )
        return redirect(reverse("product"))