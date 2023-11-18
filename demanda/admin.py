from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Demanda


# admin.py

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telefone')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)

class DemandaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'descricao', 'telefone','email', 'is_tecnico', 'data_criacao')
    search_fields = ('usuario__username', 'descricao', 'telefone','email')
    list_filter = ('is_tecnico',)

admin.site.register(Demanda, DemandaAdmin)