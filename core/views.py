from django.shortcuts import render, redirect, get_object_or_404
from .forms import FinancasForm
from .models import Financas, Venda  # Certifique-se de importar o modelo Venda
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse

def inicio(request):
    return render(request, 'core/inicio.html')

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

@login_required
def controle_financas(request):
    # Tente recuperar as finanças do usuário logado
    try:
        financas = Financas.objects.get(user=request.user)
    except Financas.DoesNotExist:
        financas = None

    # Se o formulário for enviado (POST)
    if request.method == 'POST':
        form = FinancasForm(request.POST, instance=financas)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            messages.success(request, 'Dados financeiros atualizados com sucesso!')
            return redirect('controle_financas')  # Redireciona para a mesma página ou outra após salvar
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = FinancasForm(instance=financas)

    return render(request, 'core/controle.f2.html', {'form': form, 'financas': financas})

# Função para adicionar uma venda
def adicionar_venda(request):
    if request.method == "POST":
        # Adicionando a venda no banco de dados
        produto = request.POST.get('product_name')
        quantidade = request.POST.get('quantity')
        preco_unitario = request.POST.get('unit_price')

        # Verificar se os dados foram fornecidos
        if produto and quantidade and preco_unitario:
            # Convertendo para tipos numéricos apropriados
            quantidade = int(quantidade)  # Converter quantidade para inteiro
            preco_unitario = Decimal(preco_unitario)  # Converter preco_unitario para Decimal

            # Calculando o total
            total = preco_unitario * quantidade

            # Criando e salvando a venda
            venda = Venda(
                produto=produto, 
                quantidade=quantidade, 
                preco_unitario=preco_unitario,
                total=total
            )
            venda.save()

    # Recuperando todas as vendas para exibir
    vendas = Venda.objects.all()

    # Passando as vendas para o template
    return render(request, 'core/pnegocios2.html', {'vendas': vendas})

# Função para excluir uma venda


def excluir_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
    except Venda.DoesNotExist:
        raise Http404("Venda não encontrada")

    if request.method == 'POST':
        venda.delete()
        return redirect('pnegocios2')  # Altere para a view correta
    
    return render(request, 'core/pnegocios2.html', {'venda': venda})