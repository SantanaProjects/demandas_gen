
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Demanda
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, label='Telefone')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Demanda
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, label='Telefone')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'password1', 'password2']

"""
class CustomUserCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, label='Telefone')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'password1', 'password2']
"""
class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['descricao']

    def __init__(self, *args, **kwargs):
        # Obter o usuário logado
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Definir os valores iniciais diretamente no dicionário 'initial'
        if user:
            self.initial['telefone'] = user.telefone
            self.initial['email'] = user.email

    def clean_usuario(self):
        # Certificar-se de que o campo 'usuario' está definido
        return self.instance.usuario if self.instance else None        
    