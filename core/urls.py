# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL para a página inicial
    path('', views.home, name='home'),  # Página Inicial
    
    # URL para a página de finanças pessoais
    path('financas/', views.financas, name='financas'),  # Finanças Pessoais
    
    # URL para a página de login
    path('login/', views.login_view, name='login'),  # Página de Login
    
    # Adicionando uma URL para Pequenos Negócios (se você não tiver esse app, podemos tratar de uma página simples para isso)
    path('pequenos-negocios/', views.pequenos_negocios, name='pnegocios'),  # Pequenos Negócios
    
    # Caso o "Saiba Mais" seja uma âncora, não precisa de uma URL no Django, ele será tratado apenas no HTML.
    # Mas se precisar de uma página, podemos definir uma URL aqui.
     path('saiba-mais/', views.saiba_mais, name='saiba-mais'),
]
