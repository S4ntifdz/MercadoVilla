from django.contrib import admin
from clients.models import ClientModel
# Register your models here.

#COMO VOLETIE EL MODELO DE USER QUE USA X DEFAULT DJANGO PARA VALIDAR TAMBIEN INDIRECTAMENTE VOLETIE EL ADMIN
#TENGO QUE CREAR UNO ASOCIADO AL MODELO DE USER QUE ASIGNE (EN ESTE CASO CLIENTS)

@admin.register(ClientModel)
class ClientAdmin (admin.ModelAdmin):
    pass
