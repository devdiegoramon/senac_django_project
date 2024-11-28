# core/views.py
from django.shortcuts import render


def inicio(request):
    return render(request, 'core/inicio.html')  # Rende a página inicio.html

def login_view(request):
    return render(request, 'core/login.html')

def cadastro_view(request):
    return render(request, 'core/cadastro.html')

def controlef_view(request):
    return render(request, 'core/controle.f.html')

def pnegocios_view(request):
    return render(request, 'core/pnegocios.html')

def recsenha_view(request):
    return render(request, 'core/recsenha.html')

