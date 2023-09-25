from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views 
from django.urls import include
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),  
    path('logout/', logout_then_login, name='logout'),
    path('', include('web.urls'))
]