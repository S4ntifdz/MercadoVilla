from django.urls import path
from web.views.index_view import IndexView


app_name = "web"

urlpatterns = [
    path('', IndexView.as_view(), name="product"),

]
