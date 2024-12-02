from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('', views.pnegocios2, name='pnegocios2'),
    path('adicionar_venda/', views.adicionar_venda, name='adicionar_venda'),
    path('adicionar_feedback/', views.adicionar_feedback, name='adicionar_feedback'),
    path('pnegocios2/', views.pnegocios2, name='pnegocios2'),
]
