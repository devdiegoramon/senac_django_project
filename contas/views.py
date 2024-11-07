# contas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

# View para o Cadastro (Sign Up)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automaticamente após o cadastro
            return redirect('login')  # Redireciona para a página de login
        else:
            # Caso o formulário não seja válido, você pode printar os erros para entender o que está acontecendo
            print(form.errors)  # Verifique no terminal os erros do formulário
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
                return redirect('home')  # Redireciona para a página inicial
            else:
                # Caso a autenticação falhe (usuário não encontrado ou senha incorreta)
                form.add_error(None, 'Usuário ou senha inválidos.')
        else:
            # Caso o formulário não seja válido, ele já terá erros associados a ele
            pass
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# View para o Logout
def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect('login')  # Redireciona para a página de login
