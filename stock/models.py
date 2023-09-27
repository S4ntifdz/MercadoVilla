from django.db import models
from django.contrib.auth.models import AbstractUser
#Duda:
from clients.models import ClientModel,BusinessLineChoices
# from django.contrib.auth.models import AbstractUser ?

#otra duda, esta app solo se "activaria" cuando el is_seller = True, como y cuando se valida eso?
#TODO HAY QUE USAR EL BUSINESS LINE DE CLIENTMODEL, SINO AL CAMBIAR UNO VOY A TENER QUE CAMBIAR TODOS LOS OTROS

    
class StockProduct(models.Model):
    
    user = models.ForeignKey(ClientModel,on_delete=models.CASCADE,limit_choices_to={'is_seller': True})#si se elimina un cliente, se eliminan los productos cargados por el
    business_line = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    quantity_stock = models.PositiveIntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    name_product = models.CharField(max_length=140)
    description = models.TextField(max_length=1200)
    imagen = models.ImageField(upload_to="productos", null = True)
    code_product = models.CharField(max_length=10,  primary_key=True)
    expiration = models.DateTimeField(null = True, default=None)    

    class Meta:
        unique_together = ("user","code_product")#cualquier relacion entre cliente y codigo tiene que ser unica
    
    def __str__(self): 
        return f"{self.name_product} | Seller:  {self.user} "