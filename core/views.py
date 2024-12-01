# core/views.py
from django.shortcuts import render


def inicio(request):
    return render(request, 'core/inicio.html')  # Rende a página inicio.html

def login_view(request):
    return render(request, 'contas/login.html')

def signup_view(request):
    return render(request, 'contas/signup.html')

def controlef_view(request):
    return render(request, 'core/controle.f.html')

def pnegocios_view(request):
    return render(request, 'core/pnegocios.html')

def recsenha_view(request):
    return render(request, 'core/recsenha.html')

def suporte_view(request):
    return render(request, 'core/suporte.html')

def inicio2_view(request):
    return render(request, 'core/inicio2.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def adicionar_c(request):
    return render(request, 'core/adicionar_c.html')

def banco(request):
    return render(request, 'core/banco.html')

def altsenha(request):
    return render(request, 'core/altsenha.html')

def altemail(request):
    return render(request, 'core/altemail.html')

def alteraemail1(request):
    return render(request, 'core/alteraemail1.html')

def controlef2_view(request):
    return render(request, 'core/controle.f2.html')

def erro(request):
    return render(request, 'core/erro.html')

def pnegocios2(request):
    return render(request, 'core/pnegocios2.html')
