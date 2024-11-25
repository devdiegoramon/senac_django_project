from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms

# Crie formulários personalizados, se necessário
class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm  # ou um formulário diferente

    # Outras personalizações podem ser feitas aqui
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')

# Registre o modelo com a classe CustomUserAdmin apenas se necessário
admin.site.unregister(User)  # Desregistre o User antes de registrar novamente
admin.site.register(User, UserAdmin)
