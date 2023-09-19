from django.urls import path
from signup.views import SignUpView

app_name = "signup"

urlpatterns = [
    path('', SignUpView.as_view(), name="signup"),
]
