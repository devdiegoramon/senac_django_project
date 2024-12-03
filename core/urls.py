from django.urls import path
from . import views

urlpatterns = [
    path('', views.controle_financas, name='controle_vendas'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('controle.f/', views.controlef_view, name='controle_f'),
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
    path('controle.f2/', views.controlef2_view, name='controle_f2'),
    path('erro/', views.erro, name='erro'),
    path('pnegocios2/', views.pnegocios2, name='pnegocios2'),
    path('adicionar_transacao/', views.adicionar_transacao, name='adicionar_transacao'),
    path('controle_financas/', views.controle_financas, name='controle_financas'),
]

handler404 = views.pagina_nao_encontrada
