from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from contas.forms import CustomUserCreationForm


# Logout View
def logout_view(request):
    logout(request)  # Desloga o usuário
    messages.info(request, "Você foi deslogado com sucesso.")  # Mensagem de sucesso
    return redirect('login')  # Redireciona para a página de login

# View para Cadastro (Signup)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Usando um formulário customizado (se aplicável)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")  # Mensagem de sucesso
            return redirect('home')  # Redireciona para a página inicial após o cadastro
        else:
            messages.error(request, "Houve um erro ao criar a sua conta. Tente novamente.")  # Mensagem de erro
    else:
        form = CustomUserCreationForm()  # Instanciando o formulário em GET
    return render(request, 'accounts/signup.html', {'form': form})

# View para Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")  # Mensagem de sucesso
            return redirect('home')  # Redireciona após o login
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")  # Mensagem de erro
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Página de Home (Protegida por login)
@login_required
def home(request):
    return render(request, 'home.html')  # Página inicial, somente acessível se o usuário estiver logado
