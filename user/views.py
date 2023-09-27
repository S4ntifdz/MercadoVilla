
from django.shortcuts import render
from django.views import View
from clients.models import ClientModel

class UserView(View):
    
    def get(self, request):  
        user = self.request.user 
        # si pusiera clientmodel.objects.all() me traeria todos los usuarios de la base de datos 
        #uso self.request.user para que me traiga el usuario que esta logueado
        return render(request, "user.html", {"user": user})
    
    def post(self, request):
        pass 