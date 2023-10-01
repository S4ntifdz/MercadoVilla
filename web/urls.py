from django.urls import path
from web.views.index_view import IndexView
from web.views.comunication_view import ComunicationView
#from web.views.publication_view import PublicationView





urlpatterns = [
    path('', IndexView.as_view(), name="product"),
    path('comunication/', ComunicationView.as_view(), name="comunication"),
]
