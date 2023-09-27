from django.urls import path
from publication.views import PublicationView

app_name = "publication"

urlpatterns = [
    path('', PublicationView.as_view(), name="publication"),
]
