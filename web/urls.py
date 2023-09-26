from django.urls import path
from web.views.index_view import IndexView
from web.views.publication_view import PublicationView


app_name = "web"

urlpatterns = [
    path('', IndexView.as_view(), name="product"),
    path('publication/<int:code_product>/', PublicationView.as_view(), name='publication')

]
