from django import forms
from .models import Cadastrar, Controle_financeiro, Informacoes_bancarias, Controle_de_vendas

class CadastrarForm(forms.ModelForm):
    class Meta:
        model = Cadastrar
        fields = ['email', 'nome', 'cpf', 'data_nascimento', 'senha']
class Controle_financeiroForm(forms.ModelForm):
     class Meta:
        model = Controle_financeiro
        fields = ['renda_mensal', 'gastos_fixos_mensais', 'gastos_variaveis_mensais', 'valor_investimentos', 'valor_dividas', 'valor_objeto_financeiro']
class Informacoes_bancariasForm(forms.ModelForm):
    class Meta:
        model = Informacoes_bancarias
        fields = ['banco', 'agencia', 'conta', 'codigo_confirmacao']
class Controle_de_vendasForm(forms.ModelForm):
    class Meta:
        model = Controle_de_vendas
        fields = ['valor_total_vendas_dia', 'quantidade_total_vendas', 'estoque_atual', 'lucro_estimado', 'nome_produto', 'quantidade_de_produto_vendido']
