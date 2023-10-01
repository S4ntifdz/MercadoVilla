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

class ChatView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("chat.html")
        super().__init__(**kwargs)
    
    def get(self,request):
        # stock = StockProduct.objects.get(pk=request.GET.get("item"))
        # chat = ComunicationModel.objects.filter(client_question=ClientModel.objects.get(pk=request.user.pk),client_seller=ClientModel.objects.get(pk=stock.user.pk))
        chat = ComunicationModel.objects.filter(client_question=request.user)
        context = {
            "chat" : chat,
        }
        return HttpResponse(self.template.render(context, request)) 
