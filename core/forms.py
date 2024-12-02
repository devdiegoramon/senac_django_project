from django import forms
from .models import Financas

class FinancasForm(forms.ModelForm):
    class Meta:
        model = Financas
        fields = ['renda_mensal', 'gastos_fixos', 'gastos_variaveis', 'investimentos', 'dividas', 'objetivo_financeiro']
        widgets = {
            'renda_mensal': forms.NumberInput(attrs={'class': 'form-control'}),
            'gastos_fixos': forms.NumberInput(attrs={'class': 'form-control'}),
            'gastos_variaveis': forms.NumberInput(attrs={'class': 'form-control'}),
            'investimentos': forms.NumberInput(attrs={'class': 'form-control'}),
            'dividas': forms.NumberInput(attrs={'class': 'form-control'}),
            'objetivo_financeiro': forms.Textarea(attrs={'class': 'form-control'}),
        }
