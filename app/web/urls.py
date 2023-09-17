from django.urls import path

from web.views.index_view import IndexView
# from web.views.cart_view import CartView
# from web.views.comunication_view import ComunicationView
# from web.views.comunication_interaction_view import ComunicationInteractionView
# from web.views.checkout_view import CheckoutView
app_name = "web"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
#     path('cart/', CartView.as_view(), name="cart"),
#     path('comunication/', ComunicationView.as_view(), name="comunication"),
#     path('comunication_interaction/', ComunicationInteractionView.as_view(), name="comunication_interaction"),
#     path('checkout/', CheckoutView.as_view(), name="checkout" ),
]

