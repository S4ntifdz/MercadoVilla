#  para crear un signup primero debo crear una app llamada signup
#  --> python manage.py startapp signup  
# luego debo crear un modelo de usuario que herede de AbstractUser en el archivo models.py de la app signup
# en el archivo settings.py de la app app debo agregar la app signup en la lista de apps

# luego debo agregar en el archivo settings.py de la app app la variable AUTH_USER_MODEL = "signup.User" para que django sepa que
#    el modelo de usuario es el que yo cree

# luego debo crear un archivo forms.py en la app signup para crear un formulario de registro de usuario
# luego debo crear un archivo urls.py en la app signup para crear las urls de registro de usuario
# ahi pongo la url de registro de usuario y la url de login de usuario, por ejemplo:
# path('signup/', SignUpView.as_view(), name="signup"),
# path('login/', LoginView.as_view(), name="login"),

# luego debo crear un archivo views.py en la app signup para crear las vistas de registro de usuario
# ahi pongo la vista de registro de usuario y la vista de login de usuario, por ejemplo:
# class SignUpView(CreateView):
#     form_class = SignUpForm
#     template_name = "signup/signup.html"
#     success_url = reverse_lazy("login")

# class LoginView(FormView):
#     form_class = LoginForm
#     template_name = "signup/login.html"
#     success_url = reverse_lazy("web:index")
#     def form_valid(self, form):
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return super().form_valid(form)

# luego debo crear un archivo urls.py en la app app para crear las urls de registro de usuario
# ahi pongo la url de registro de usuario y la url de login de usuario, por ejemplo:
# path('', include('signup.urls')),
# path("accounts/", include("django.contrib.auth.urls")),
# path("", include("web.urls")),
# path('admin/', admin.site.urls),

# luego debo crear un archivo index.html en la app web en la carpeta templates/web para crear la pagina de inicio
# luego debo crear un archivo index_view.py en la app web en la carpeta views para crear la vista de la pagina de inicio
# luego debo crear un archivo urls.py en la app web para crear las urls de la pagina de inicio
# ahi pongo la url de la pagina de inicio, por ejemplo:
# path('', IndexView.as_view(), name="index"),

# luego debo crear un archivo index.html en la app web en la carpeta templates/web para crear la pagina de inicio
# luego debo crear un archivo index_view.py en la app web en la carpeta views para crear la vista de la pagina de inicio