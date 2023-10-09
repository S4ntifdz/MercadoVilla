"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#.................................
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", include("signup.urls")),
    path('login/', include('login.urls')),
    path('web/', include('web.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("user/", include("user.urls")),
    path("publication/<int:code_product>", include("publication.urls")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("cart/", include("cart.urls")),
    path("", views.IndexView.as_view())
]
if settings.DEBUG: #aca pregunto si estoy en debug, ya que nunca me dejaria hacerlo en produccion
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

