from django import forms
from .models import Financas
from .models import Venda

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

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'quantidade', 'preco_unitario']

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade