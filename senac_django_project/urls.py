# senac_django_project/urls.py
from django.contrib import admin, path
from django.urls import path, include  # "include" importa as URLs de outros apps
from django.shortcuts import redirect

def redirect_home(request):
    return redirect('home')  # Ou 'home/' se a URL não for nomeada


urlpatterns = [
    path('', redirect_home),  # Redireciona para a view 'home'
    path('admin/', admin.site.urls),
    # Aqui, você inclui as URLs do app 'accounts' que foi definido no arquivo de urls do app
    path('accounts/', include('contas.urls')),  # Certifique-se que 'contas' é o nome do seu app

    path('core/', include('core.urls')),
]
