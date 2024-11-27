from django import forms
from .models import Usuario, Financas_pessoas, Informacoes_bancarias, Vendas, Pequeno_negocio

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
        fields = ['razao_social', 'responsavel', 'vategoria', 'renda_mensal', 'despesas_fixas', 'despesas_variaveis']

