from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('controle.f/', views.controlef_view, name='controle.f'),
    path('pnegocios/', views.pnegocios_view, name='pnegocios'),
    path('recsenha/', views.recsenha_view, name='recsenha'),
    path('suporte/', views.suporte_view, name='suporte'),
    path('inicio2/', views.inicio2_view, name='inicio2'),
    path('perfil/', views.perfil, name='perfil'),
    path('adicionar_c/', views.adicionar_c, name='adicionar_c'),
    path('banco/', views.banco, name='banco'),
    path('altsenha/', views.altsenha, name='altsenha'),
    path('altemail/', views.altemail, name='altemail'),
    path('alteraemail1/', views.altemail, name='altemail1'),
    path('controle.f2/', views.controlef2_view, name='controle.f2'),
    path('erro/', views.erro, name='erro'),
    path('pnegocios2/', views.pnegocios2, name='pnegocios2'),
    path('controle_financas/', views.controle_financas, name='controle_financas'),
    path('venda/excluir/<int:venda_id>/', views.excluir_venda, name='excluir_venda'),
  # Página principal de vendas
    path('', views.controle_financas, name='controle_vendas'),

]
