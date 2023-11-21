

#  views.py


from django.contrib.auth import authenticate, login
from .forms import LoginForm, DemandaForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import logging
from django.contrib.auth import logout
from .models import Demanda
from django.utils import timezone
from datetime import datetime
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)


def enviar_email_nova_demanda(demanda):
    # Configurações de e-mail
    subject = 'Nova Demanda Criada'
    message = f'Uma nova demanda foi criada por {demanda.usuario.username}. Detalhes:\n\nTelefone: {demanda.telefone}\nProblema: {demanda.descricao}'
    from_email = settings.DEFAULT_FROM_EMAIL

    # Lista de destinatários
    to_email = settings.EMAIL_RECEPIENT

    try:
        # Enviar e-mail
        email = EmailMessage(subject, message, from_email, to_email)
        email.send()
        logger.info(f'E-mail enviado com sucesso para {", ".join(to_email)}')
    except Exception as e:
        logger.error(f'Erro ao enviar e-mail: {str(e)}')

"""
# Verifica se o usuário está autenticado, redirecionando-o para a página de login se não estiver.
@login_required(login_url='user_login')
def criar_demanda(request):
    # Verifica novamente a autenticação para garantir que o usuário está autenticado.
    if request.user.is_authenticated:
        # Cria uma instância do formulário de demanda, passando o usuário autenticado como parâmetro.
        form = DemandaForm(user=request.user)

        # Verifica se o método da requisição é POST (envio de formulário).
        if request.method == 'POST':
            # Cria uma instância do formulário com os dados do POST, incluindo o usuário autenticado.
            form = DemandaForm(request.POST, user=request.user)
            
            # Verifica se o formulário é válido.
            if form.is_valid():
                # Salva a demanda no banco de dados, associando-a ao usuário autenticado.
                demanda = form.save(commit=False)
                demanda.usuario = request.user
                demanda.save()

                # Exibe uma mensagem de sucesso para o usuário.
                messages.success(request, 'A demanda foi criada com sucesso!')
                # Envia um e-mail para destinatários informando sobre a nova demanda.
                enviar_email_nova_demanda(demanda)

                # Cria um contexto com a variável 'sucesso' para ser usada no template 'aviso.html'.
                context = {'sucesso': True}
                # Renderiza o template 'aviso.html' com o contexto, exibindo a mensagem de sucesso.
                return render(request, 'aviso.html', context)

        else:
            # Se o método da requisição não for POST, mantém o formulário de demanda para exibição.
            form = DemandaForm(user=request.user)
        # Renderiza o template 'criar_demanda.html' com o formulário de demanda.
        return render(request, 'criar_demanda.html', {'form': form})
    else:
        # Se o usuário não estiver autenticado, redireciona para a página de login.
        return redirect('user_login')

"""

def custom_logout(request):
    # Chame a função de logout do Django
    logout(request)
    # Redirecione para onde desejar após o logout
    return redirect('user_login')



logger = logging.getLogger(__name__)
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_tecnico:
                    return redirect('dashboard_tecnico')
                else:
                    return redirect('criar_demanda')
            else:
                form.add_error(None, 'Nome de usuário ou senha inválidos.')
    else:
        form = LoginForm()

    # Se o usuário está autenticado, redirecione para a página apropriada
    if request.user.is_authenticated:
        if request.user.is_tecnico:
            return redirect('dashboard_tecnico')
        else:
            return redirect('criar_demanda')

    return render(request, 'login.html', {'form': form})



def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_tecnico = form.cleaned_data['is_tecnico']
            user.save()
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadastro.html', {'form': form})




@login_required
def dashboard_tecnico(request):
    data_criacao_inicio = request.GET.get('data_criacao_inicio')
    data_criacao_fim = request.GET.get('data_criacao_fim')

    # Verifique se as datas são diferentes de None antes de converter
    if data_criacao_inicio and data_criacao_fim:
        # Converta as datas de string para objetos datetime usando parse_date
        data_criacao_inicio = make_aware(datetime.combine(parse_date(data_criacao_inicio), datetime.min.time()))
        data_criacao_fim = make_aware(datetime.combine(parse_date(data_criacao_fim), datetime.max.time()))

        # Faça a filtragem das demandas usando as datas ajustadas
        demandas = Demanda.objects.filter(data_criacao__range=(data_criacao_inicio, data_criacao_fim))
    else:
        # Se as datas forem None, retorne todas as demandas
        demandas = Demanda.objects.all()

    # Adicione esta linha para imprimir as datas e verificar se estão corretas
    print("Data de início:", data_criacao_inicio)
    print("Data de fim:", data_criacao_fim)

    return render(request, 'dashboard_tecnico.html', {'demandas': demandas})



@login_required(login_url='user_login')
def criar_demanda(request):
    if request.user.is_authenticated:
        form = DemandaForm(user=request.user)

        if request.method == 'POST':
            form = DemandaForm(request.POST, user=request.user)
            
            if form.is_valid():
                demanda = form.save(commit=False)
                demanda.usuario = request.user
                demanda.status = 'AB'  # Definindo o status como "Aberta"
                demanda.save()

                messages.success(request, 'A demanda foi criada com sucesso!')
                enviar_email_nova_demanda(demanda)

                context = {'sucesso': True}
                return render(request, 'aviso.html', context)

        else:
            form = DemandaForm(user=request.user)

        return render(request, 'criar_demanda.html', {'form': form})
    else:
        return redirect('user_login')
    

@login_required(login_url='user_login')
def marcar_atendida(request, demanda_id):
    demanda = get_object_or_404(Demanda, pk=demanda_id)

    # Verifique se o usuário autenticado é um técnico
    if request.user.is_authenticated and request.user.is_tecnico:
        # Obtenha o novo status do formulário POST
        novo_status = request.POST.get('status', 'AB')  # 'AB' é o valor padrão se não for especificado

        # Apenas atualize o status se for um valor válido
        if novo_status in [opcao[0] for opcao in Demanda.STATUS_CHOICES]:
            demanda.status = novo_status
            demanda.save()
            messages.success(request, 'O status da demanda foi atualizado com sucesso!')
        else:
            messages.error(request, 'O status especificado não é válido.')
    else:
        messages.error(request, 'Você não tem permissão para marcar esta demanda como atendida.')

    return redirect('dashboard_tecnico')