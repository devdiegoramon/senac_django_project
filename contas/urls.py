# contas/urls.py
from . import views
from django.urls import path

urlpatterns = [
    # URL para login (padrão do Django)
    path('login/', views.login_view, name='login'),
    
    # URL para logout (usando a view personalizada)
    path('logout/', views.logout_view, name='logout'),
    
    # URL para signup (cadastro de novo usuário)
    path('signup/', views.signup, name='signup'),

    # URL para a home, protegida por login
    path('home/', views.home, name='home'),
]
