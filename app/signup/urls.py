from django.urls import path
from signup.views import SignUpView
app_name = "signup"
urlpatterns = [
    path('signup', SignUpView.as_view(), name="signup"),
]
