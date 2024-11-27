from django.db import models
from datetime import datetime #importando data atual

class Usuario(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DataField(max_length=15)
    senha = models.CharField()


class Financas_pessoas(models.Model):
    renda_mensal = models.DecimalField()
    gastos_fixos_mensais = models.DecimalField()
    gastos_variaveis_mensais = models.DecimalField()
    valor_investimentos = models.DecimalField()
    valor_dividas = models.DecimalField()
    valor_objeto_financeiro = models.DecimalField()
    #index fk_usuario

class Informacoes_bancarias(models.Model):
    banco = models.IntergerField()
    agencia = models.IntergerField()
    conta = models.IntergerField()
    saldo = models.DecimalField()
    codigo_confirmacao = models.IntergerField()
    #index fk_usuario
    #index fk_pequeno_negocio

#Novos
class Vendas(models.Model):
    nome_produto = models.CharField(max_length=150)
    quantidade_de_produto_vendido = models.IntergerField()#quantidade do um produto vendido numa venda expecifica
    preco = models.DecimalField()
    data_da_venda = models.date.today()
    status = models.CharField(max_length=50)
    #index fk_pequeno_negocio

class Pequeno_negocio(models.Model):
    razao_social = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=45)
    vategoria = models.CharField(max_length=50)
    renda_mensal = models.DecimalField()
    despesas_fixas = models.DecimalField()
    despesas_variaveis = models.DecimalField()
    #index fk_Financas_pessoas
