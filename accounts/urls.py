from django.urls import path
from django.contrib.auth.views import login
from simplemooc.accounts.views import register

app_name = "accounts"

urlpatterns = [
    path('entrar/', login, {'template_name':'accounts/login.html'}, name="login"),
    path('cadastrar/', register, name="register"),
]