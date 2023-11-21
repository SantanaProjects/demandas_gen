
#URLS.PY   

                
from django.urls import path,include
from .views import user_login, criar_demanda,cadastro,custom_logout,dashboard_tecnico,marcar_atendida


urlpatterns = [
  
    path('', user_login, name='user_login'),
    path('criar_demanda', criar_demanda, name='criar_demanda'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', custom_logout, name='logout'),
    path('dashboard_tecnico', dashboard_tecnico, name='dashboard_tecnico'),
    path('marcar_atendida/<int:demanda_id>/', marcar_atendida, name='marcar_atendida'),
]


