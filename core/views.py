# core/views.py
from django.shortcuts import render

# Função que renderiza a página inicial
def home(request):
    return render(request, 'core/home.html')  # Certifique-se de que 'home.html' está em 'core/templates/core/'

# Função que renderiza a página de finanças pessoais
def financas(request):
    return render(request, 'core/controle-financeiro.html')  # Certifique-se de que 'controle-financeiro.html' está em 'core/templates/core/'

# Função que renderiza a página de login
def login_view(request):
    return render(request, 'core/login.html')  # Substitua pelo caminho correto para o seu template de login


##as views abaixo estao erradas, trocar para o nome dos htmls certos. estao ai so pra testes.

# Função que renderiza a página de pequenos negócios (Se você não tem uma página específica, crie uma nova view ou remova)
def pequenos_negocios(request):
    return render(request, 'core/painel-negocios.html')  # Certifique-se de ter uma página de 'pequenos_negocios.html' ou ajuste conforme necessário

# Função que renderiza a seção "Saiba Mais" ou uma página que você tenha para isso
def saiba_mais(request):
    return render(request, 'core/saiba_mais.html')  # Certifique-se de ter uma página 'saiba_mais.html' ou ajuste conforme necessário
def saiba_mais(request):
    return render(request, 'core/saiba_mais.html')