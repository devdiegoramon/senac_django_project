from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Financas_pessoas, Informacoes_bancarias, Vendas, Pequeno_negocio

# Formulário personalizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Seus outros formulários permanecem os mesmos
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'cpf', 'data_nascimento', 'senha']

class Financas_pessoasForm(forms.ModelForm):
    class Meta:
        model = Financas_pessoas
        fields = ['renda_mensal', 'gastos_fixos_mensais', 'gastos_variaveis_mensais', 'valor_investimentos', 'valor_dividas', 'valor_objeto_financeiro']

class Informacoes_bancariasForm(forms.ModelForm):
    class Meta:
        model = Informacoes_bancarias
        fields = ['banco', 'agencia', 'conta', 'codigo_confirmacao']

class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome_produto', 'quantidade_de_produto_vendido', 'preco', 'data_da_venda', 'status']

class Pequeno_negocioForm(forms.ModelForm):
    class Meta:
        model = Pequeno_negocio
        fields = ['razao_social', 'responsavel', 'categoria', 'renda_mensal', 'despesas_fixas', 'despesas_variaveis']
