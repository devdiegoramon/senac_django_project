from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contas.models import Vendas


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    cpf = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    data_nascimento = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        fields = ['username', 'email', 'cpf', 'data_nascimento', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    email = forms.CharField(
        label="Email/Usuario", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    )
    senha = forms.CharField(
        label="Senha", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''})
    )


#models de vendas

class VendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome_produto', 'quantidade_de_produto_vendido', 'preco', 'data_da_venda', 'status']  # Campos do modelo
        widgets = {
            'nome_produto': forms.TextInput(attrs={'placeholder': 'Nome do Produto'}),
            'quantidade_de_produto_vendido': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'preco': forms.NumberInput(attrs={'placeholder': 'Preço Unitário', 'step': '0.01'}),
            'data_da_venda': forms.DateInput(attrs={'type': 'date'}),  # Widget de data
            'status': forms.TextInput(attrs={'placeholder': 'Status da Venda'}),
        }
