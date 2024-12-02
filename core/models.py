from django.db import models
from django.contrib.auth.models import User

class Financas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Tornar o campo opcional
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gastos_fixos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gastos_variaveis = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    investimentos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dividas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    objetivo_financeiro = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Finanças de {self.user.username}'
