# senac_django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core.views import inicio  # Importe a view 'home' do módulo 'core'
from django.conf.urls import handler404, handler500
from core import views as core_views

# Configuração para tratamento de erros
handler404 = core_views.pagina_nao_encontrada
handler500 = core_views.erro_interno

def redirect_home(request):
    return redirect('inicio')  # Redireciona para a URL nomeada 'home'

urlpatterns = [
    path('', redirect_home),  # Redireciona para a view 'home'
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),  # A URL para a página inicial
    path('accounts/', include('contas.urls')),  # Certifique-se de que 'contas' é o nome do seu app
    path('core/', include('core.urls')),  # Incluir as URLs do app 'core'
    path('contas/', include('contas.urls')),  # Incluir as URLs do app 'core'
]