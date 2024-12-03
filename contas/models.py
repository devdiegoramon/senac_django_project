from django.db import models
from datetime import datetime

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(default=datetime.today)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


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

class Venda(models.Model):
    produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venda {self.id} - {self.produto}"

class Feedback(models.Model):
    feedback = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id}"