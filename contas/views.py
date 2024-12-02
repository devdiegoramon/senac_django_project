from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import VendaForm 

# Função de criação de conta
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automaticamente após o cadastro
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('inicio2')  # Redireciona para a página inicial ou onde for necessário
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            print(form.errors)  # Verifique no terminal os erros do formulário
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Função de login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['senha']
            
            # Autenticando o usuário
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Inicia a sessão do usuário
                messages.success(request, 'Bem-vindo!')
                return redirect('inicio2')  # Redireciona para a página principal
            else:
                messages.error(request, 'Credenciais inválidas.')
                return redirect('login')  # Redireciona de volta para a página de login
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# Função de logout
def user_logout(request):
    logout(request)
    messages.info(request, 'Você foi desconectado.')
    return redirect('login')

def adicionar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a venda no banco de dados
            mensagem = "Venda adicionada com sucesso!"
            return redirect('pnegocios2')  # Redireciona para a página de vendas
        else:
            mensagem = "Erro ao adicionar venda! Verifique os campos."
    else:
        form = VendaForm()

    # Se a requisição for GET ou o formulário não for válido, mostramos a página com o formulário.
    return render(request, 'core/pnegocios2.html', {'form': form, 'mensagem': mensagem})