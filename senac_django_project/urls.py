# senac_django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # "include" importa as URLs de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Aqui, você inclui as URLs do app 'accounts' que foi definido no arquivo de urls do app
    path('accounts/', include('contas.urls')),  # Certifique-se que 'contas' é o nome do seu app
]
