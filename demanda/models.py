# models.py


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models


"""
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    is_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Demanda(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_tecnico = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def extract_image_urls(self):
        # Processar a descrição para extrair URLs de imagens
        import re
        pattern = re.compile(r'https?://[^\s]+')
        return pattern.findall(self.descricao)

    def __str__(self):
        return f'Demanda de {self.usuario.username}: {self.descricao}'


@receiver(pre_save, sender=Demanda)
def set_data_criacao(sender, instance, **kwargs):
    if not instance.data_criacao:
        instance.data_criacao = timezone.now()
    
    if instance.usuario:
        instance.telefone = instance.usuario.telefone
        instance.email = instance.usuario.email
"""       
from django.contrib.auth import get_user_model
from django.db import models

#CustomUser = get_user_model()

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    is_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Demanda(models.Model):
    STATUS_CHOICES = [
        ('AB', 'Aberta'),
        ('AT', 'Atendida'),
    ]

    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao = models.TextField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_tecnico = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AB')

    def extract_image_urls(self):
        # Processar a descrição para extrair URLs de imagens
        import re
        pattern = re.compile(r'https?://[^\s]+')
        return pattern.findall(self.descricao)

    def __str__(self):
        return f'Demanda de {self.usuario.username}: {self.descricao}'
    

@receiver(pre_save, sender=Demanda)
def set_data_criacao(sender, instance, **kwargs):
    if not instance.data_criacao:
        instance.data_criacao = timezone.now()
    
    if instance.usuario:
        instance.telefone = instance.usuario.telefone
        instance.email = instance.usuario.email
