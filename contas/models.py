from django.db import models
from datetime import datetime

class Usuario(models.Model):
    email = models.EmailField(unique=True)  # Adicionando unique=True para garantir que não haja emails duplicados
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)  # Adicionando unique=True para garantir CPFs únicos
    data_nascimento = models.DateField(default=datetime.today)
    senha = models.CharField(max_length=128)  # Definindo um tamanho razoável para a senha

    def __str__(self):
        return self.nome

class Financas_pessoas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='financas')
    renda_mensal = models.DecimalField(max_digits=15, decimal_places=2)
    gastos_fixos_mensais = models.DecimalField(max_digits=15, decimal_places=2)
    gastos_variaveis_mensais = models.DecimalField(max_digits=15, decimal_places=2)
    valor_investimentos = models.DecimalField(max_digits=15, decimal_places=2)
    valor_dividas = models.DecimalField(max_digits=15, decimal_places=2)
    valor_objeto_financeiro = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Finanças de {self.usuario.nome}"

class Informacoes_bancarias(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='informacoes_bancarias')
    banco = models.IntegerField()
    agencia = models.IntegerField()
    conta = models.IntegerField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    codigo_confirmacao = models.IntegerField()

    def __str__(self):
        return f"Informações bancárias de {self.usuario.nome}"

class Vendas(models.Model):
    nome_produto = models.CharField(max_length=150)
    quantidade_de_produto_vendido = models.IntegerField()
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    data_da_venda = models.DateField(default=datetime.today)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Venda do produto {self.nome_produto}"

class Pequeno_negocio(models.Model):
    razao_social = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=45)
    categoria = models.CharField(max_length=50)
    renda_mensal = models.DecimalField(max_digits=15, decimal_places=2)
    despesas_fixas = models.DecimalField(max_digits=15, decimal_places=2)
    despesas_variaveis = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Pequeno Negócio: {self.razao_social}"
