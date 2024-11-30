# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('controle.f/', views.controlef_view, name='controle.f'),
    path('pnegocios/', views.pnegocios_view, name='pnegocios'),
    path('recsenha/', views.recsenha_view, name='recsenha'),
]

