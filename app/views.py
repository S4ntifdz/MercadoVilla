from django.shortcuts import render
from django.views import View
from stock.models import StockProduct
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin    
from django.shortcuts import render, get_object_or_404

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')