from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Financas, Venda, Transacao
from .forms import FinancasForm
import logging

logger = logging.getLogger(__name__)

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

def controlef2_view(request):
    # Lógica para exibir a página controlef2
    return render(request, 'core/controle.f2.html')

def erro(request):
    # Exibe uma página de erro
    return render(request, 'core/erro.html')


def pnegocios2(request):
    return render(request, 'core/pnegocios2.html')


# Função para adicionar transação
def adicionar_transacao(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')

        logger.debug(f"Recebendo transação - Descrição: {descricao}, Valor: {valor}, Categoria: {categoria}")

        if descricao and valor:
            try:
                # Salvar a transação no banco de dados
                Transacao.objects.create(descricao=descricao, valor=valor, categoria=categoria)
                
                # Exibir mensagem de sucesso
                messages.success(request, 'Transação salva com sucesso!')
                return redirect('core:adicionar')  # Substitua com o nome correto da URL

            except Exception as e:
                # Exibir mensagem de erro
                messages.error(request, f'Ocorreu um erro ao salvar a transação: {e}')
        else:
            # Exibir mensagem de erro caso faltem campos obrigatórios
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')

    # Buscar todas as transações
    transacoes = Transacao.objects.all()

    return render(request, 'core/adicionar_transacao.html', {'transacoes': transacoes})

# Função para exibir a página de inicio
def inicio(request):
    return render(request, 'core/inicio.html')

# Função de login
def login_view(request):
    return render(request, 'contas/login.html')

# Função de signup
def signup_view(request):
    return render(request, 'contas/signup.html')

# Funções para controle de finanças
@login_required
def controle_financas(request):
    try:
        financas = Financas.objects.get(user=request.user)
    except Financas.DoesNotExist:
        financas = None

    if request.method == 'POST':
        form = FinancasForm(request.POST, instance=financas)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados financeiros atualizados com sucesso!')
            return redirect('controle_financas')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = FinancasForm(instance=financas)

    return render(request, 'core/controle.f2.html', {'form': form, 'financas': financas})

# Função para adicionar venda
def adicionar_venda(request):
    if request.method == "POST":
        produto = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade'))
        preco_unitario = float(request.POST.get('preco_unitario'))
        total = quantidade * preco_unitario

        venda = Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=preco_unitario,
            total=total,
            status='Finalizada'
        )

        return JsonResponse({
            'status': 'success',
            'id': venda.id,
            'produto': venda.produto,
            'quantidade': venda.quantidade,
            'total': venda.total
        })

    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)

# Função para excluir venda
def excluir_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
    except Venda.DoesNotExist:
        raise 404("Venda não encontrada")

    if request.method == 'POST':
        venda.delete()
        return redirect('pnegocios2')

    return render(request, 'core/pnegocios2.html', {'venda': venda})

# Função para página 404
def pagina_nao_encontrada(request, exception):
    return render(request, 'core/erro.html', status=404)

# Função para erro interno
def erro_interno(request):
    return render(request, 'core/erro.html', status=500)
