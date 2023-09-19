from django.urls import path
from . import views  # Asegúrate de que esta importación sea correcta

urlpatterns = [
    # Otras rutas de URL aquí
    path('', views.LoginView.as_view(), name='login'),  # Asigna la vista de la clase LoginView
    # Otras rutas de URL aquí
    #no me abre el login ene l navegador po
]