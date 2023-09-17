# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.models import StockProduct

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        template = loader.get_template("index.html")
        stock_by_interes = StockProduct.objects.filter(business_line=request.user.business_line_interes).exclude(client=request.user)
        context = {
            "stock": stock_by_interes,
        }
        return HttpResponse(template.render(context, request))