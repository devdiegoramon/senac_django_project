from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core.views import home  # Importe a view 'home' do módulo 'core'

def redirect_home(request):
    return redirect('home')  # Redireciona para a URL nomeada 'home'

urlpatterns = [
    path('', redirect_home),  # Redireciona para a view 'home'
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  # A URL para a página inicial
    path('accounts/', include('contas.urls')),  # Certifique-se de que 'contas' é o nome do seu app
    path('core/', include('core.urls')),  # Incluir as URLs do app 'core'
]
