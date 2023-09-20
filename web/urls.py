from django.urls import path
from web.views import ProductView

app_name = "web"

urlpatterns = [
    path('', ProductView.as_view(), name="product"),
]
