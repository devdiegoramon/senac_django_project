# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm  # Certifique-se de ter um formulário para o Signup
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect('login')  # Redireciona para a página de login



# View para Cadastro (Signup)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})  # Verifique o caminho do template


# View para Login (Usando a view padrão do Django)
# A view de login padrão já está configurada em urls.py
# Não é necessário escrever a view, mas vamos deixar aqui caso queira customizar.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona após o login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View para logout (Você já pode usar a view padrão do Django para logout)
# Se for usar a view padrão, não precisa de código aqui, só configura na URL
# Para redirecionar após o logout, use: LOGOUT_REDIRECT_URL = '/accounts/login/'

# Página de Home (Protegida por login)
@login_required
def home(request):
    return render(request, 'home.html')
