from django.shortcuts import render

# Função que renderiza a página inicial
def home(request):
    return render(request, 'core/home.html')  # Certifique-se de que 'home.html' está em 'core/templates/core/'
