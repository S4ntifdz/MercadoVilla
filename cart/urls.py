from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    # Agrega otras URLs relacionadas con el carrito, como agregar y eliminar elementos
]
