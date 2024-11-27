from django.db import models

class Cadastrar(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DataField(max_length=15)
    senha = models.CharField()


class Controle_financeiro(models.Model):
    renda_mensal = models.DecimalField()
    gastos_fixos_mensais = models.DecimalField()
    gastos_variaveis_mensais = models.DecimalField()
    valor_investimentos = models.DecimalField()
    valor_dividas = models.DecimalField()
    valor_objeto_financeiro = models.DecimalField()

class Informacoes_bancarias(models.Model):
    banco = models.CharField(max_length=150)
    agencia = models.IntergerField()
    conta = models.IntergerField()
    codigo_confirmacao = models.IntergerField()

class Controle_de_vendas(models.Model):
    valor_total_vendas_dia = models.DecimalField()
    quantidade_total_vendas = models.IntergerField()#quantidade total de vendas por todos os produtos
    estoque_atual  = models.IntergerField()
    lucro_estimado = models.DecimalField()
    nome_produto = models.CharField(max_length=150)
    quantidade_de_produto_vendido = models.IntergerField() #quantidade do um produto vendido numa venda expecifica
