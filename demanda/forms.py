#ARQUIVO FORMS.PY

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Demanda
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    
    # Adicione o campo de telefone com a classe personalizada
   # telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'telefone-input'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'telefone'}))
    is_tecnico = forms.BooleanField(required=False, label='É Técnico?')
    #telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'telefone-input'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'is_tecnico', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class DemandaForm(forms.ModelForm):
    is_tecnico = forms.BooleanField(required=False, label='É Técnico?', initial=False)

    class Meta:
        model = Demanda
        fields = ['descricao', 'is_tecnico']

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

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        # Processar a descrição para extrair URLs de imagens
        import re
        pattern = re.compile(r'https?://[^\s]+')
        image_urls = pattern.findall(descricao)
        # Faça algo com as URLs, se necessário
        return descricao 
    