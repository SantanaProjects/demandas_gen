# models.py


"""
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Demanda(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15)
    is_tecnico = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Demanda de {self.usuario.username}: {self.descricao}'

# Sinal para definir a data de criação antes de salvar a instância do modelo
@receiver(pre_save, sender=Demanda)
def set_data_criacao(sender, instance, **kwargs):
    if not instance.data_criacao:
        instance.data_criacao = timezone.now()
"""
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Demanda(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_tecnico = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Demanda de {self.usuario.username}: {self.descricao}'

# Sinal para definir a data de criação antes de salvar a instância do modelo
@receiver(pre_save, sender=Demanda)
def set_data_criacao(sender, instance, **kwargs):
    if not instance.data_criacao:
        instance.data_criacao = timezone.now()
    
    # Preencher os campos de telefone e email com os valores do usuário associado
    if instance.usuario:
        instance.telefone = instance.usuario.telefone
        instance.email = instance.usuario.email
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Demanda(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_tecnico = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Demanda de {self.usuario.username}: {self.descricao}'

@receiver(pre_save, sender=Demanda)
def set_data_criacao(sender, instance, **kwargs):
    if not instance.data_criacao:
        instance.data_criacao = timezone.now()
    
    if instance.usuario:
        instance.telefone = instance.usuario.telefone
        instance.email = instance.usuario.email