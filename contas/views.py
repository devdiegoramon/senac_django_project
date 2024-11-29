from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# View para o Cadastro (Sign Up)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automaticamente após o cadastro
            return redirect('home')  # Redireciona para a página inicial ou qualquer outra página desejada
        else:
            # Caso o formulário não seja válido, exiba os erros no terminal
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# View para o Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autentica o usuário com os dados do formulário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # Verifica se o usuário foi autenticado
            if user is not None:
                login(request, user)  # Realiza o login
                return redirect('home')  # Redireciona para a página inicial ou outra página desejada
            else:
                # Caso a autenticação falhe (usuário não encontrado ou senha incorreta)
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# View para o Logout
def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect('login')  # Redireciona para a página de login
