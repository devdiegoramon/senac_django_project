from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Venda, Feedback
from django.http import JsonResponse
import json
from datetime import datetime
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


#abaixo a tentativa de bd do pgnegocios

def pnegocios2(request):
    vendas = Venda.objects.all().order_by('-data_venda')
    total_vendas = sum(venda.total for venda in vendas)
    vendas_hoje = vendas.filter(data_venda__date=datetime.today().date()).count()
    estoque_atual = 50  # Exemplo estático, você pode personalizar isso
    lucro_estimado = total_vendas  # Como exemplo, consideramos o total de vendas como lucro estimado
    vendas = Venda.objects.all().order_by('-data_venda')


    context = {
        'vendas': vendas,
        'total_vendas': total_vendas,
        'vendas_hoje': vendas_hoje,
        'estoque_atual': estoque_atual,
        'lucro_estimado': lucro_estimado,
    }

    return render(request, 'core/pnegocios2.html', context)

# View para adicionar uma nova venda
def adicionar_venda(request):
    if request.method == 'POST':
        produto = request.POST.get('product_name')
        quantidade = int(request.POST.get('quantity'))
        preco_unitario = float(request.POST.get('unit_price'))
        
        venda = Venda(produto=produto, quantidade=quantidade, preco_unitario=preco_unitario)
        venda.save()

        return redirect('pnegocios2')

    return redirect('pnegocios2')  # Em caso de método diferente de POST, volta para a página de vendas

# View para enviar feedback
@csrf_exempt  # Usado para testar, mas em produção, o CSRF deve ser tratado corretamente
def adicionar_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Captura o feedback enviado como JSON
        feedback_text = data.get('feedback')

        feedback = Feedback(feedback=feedback_text)
        feedback.save()

        return JsonResponse({'status': 'success', 'message': 'Feedback enviado com sucesso!'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido'})




def pnegocios2(request):
    # Recupera todas as vendas ordenadas pela data
    vendas = Venda.objects.all().order_by('-data_venda')

    # Calcula o total de vendas
    total_vendas = sum(venda.total for venda in vendas)

    # Filtra vendas realizadas hoje
    vendas_hoje = vendas.filter(data_venda__date=datetime.today().date()).count()

    # Exemplo de estoque (ajuste conforme sua lógica de estoque)
    estoque_atual = 50  # Pode ser substituído por lógica dinâmica

    # Exemplo de cálculo de lucro (ajuste conforme necessário)
    lucro_estimado = total_vendas  # Aqui pode incluir descontos, custos, etc.

    # Cria o contexto para enviar os dados ao template
    context = {
        'vendas': vendas,
        'total_vendas': total_vendas,
        'vendas_hoje': vendas_hoje,
        'estoque_atual': estoque_atual,
        'lucro_estimado': lucro_estimado,
    }

    return render(request, 'core/pnegocios2.html', context)

def excluir_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
    except Venda.DoesNotExist:
        raise Http404("Venda não encontrada")

    if request.method == 'POST':
        venda.delete()
        return redirect('pnegocios2')  # Altere para a view correta
    
    return render(request, 'core/pnegocios2.html', {'venda': venda})