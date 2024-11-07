# core/urls.py
from django.urls import path
from . import views  # Verifique se as views estão importadas corretamente

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
]
