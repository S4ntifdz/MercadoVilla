from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import ComunicationModel
# Register your models here.

@admin.register(ComunicationModel)
class ComunicationAdmin(admin.ModelAdmin):
    list_display = ("client_question","client_seller","is_answer")
    
    def is_answer(self, value):
        return bool(value.answer)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        #solo muestro las preguntas que no tienen respuesta
        return super().get_queryset(request).filter(client_seller=request.user) #filtro por el usuario logueado