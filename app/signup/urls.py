# from django.urls import path
# from . import views

# urlpatterns = [
#     # Otras URLs existentes
#     path('signup/', views.signup_view, name='signup'),
#     path('signup2/', views.signup_view, name='signup2'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('signup/step1/', views.signup_step1, name='signup_step1'),
    path('signup/step2/', views.signup_step2, name='signup_step2'),
    # Agrega una URL para la página de éxito si lo deseas
]

