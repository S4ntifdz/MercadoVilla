
from django.urls import path
from web.views.index_view import IndexView
#from web.views.publication_view import PublicationView
from cart.views import CartView




urlpatterns = [
    path('', CartView.as_view(), name="cart"),
]
