import logging
from django.contrib.auth import authenticate, login
from .forms import LoginForm, DemandaForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


logger = logging.getLogger(__name__)
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('criar_demanda')  # página após o login
            else:
                form.add_error(None, 'Nome de usuário ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



# Modifique a view criar_demanda
@login_required(login_url='user_login')
def criar_demanda(request):
    # Verifique se o usuário está autenticado
    if request.user.is_authenticated:
        # Preencha o formulário com os dados do usuário logado
        form = DemandaForm(user=request.user)
        if request.method == 'POST':
            form = DemandaForm(request.POST, user=request.user)
            if form.is_valid():
                demanda = form.save(commit=False)
                demanda.usuario = request.user
                demanda.save()

                # Exibir mensagem de sucesso
                messages.success(request, 'A demanda foi criada com sucesso!')

                # Enviar e-mail para destinatários
                enviar_email_nova_demanda(demanda)

                return redirect('criar_demanda')
        else:
            form = DemandaForm(user=request.user)

        return render(request, 'criar_demanda.html', {'form': form})
    else:
        return redirect('user_login')
    



"""
def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a página desejada após o cadastro bem-sucedido
            return redirect('user_login')  # ajuste aqui para a página desejada
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadastro.html', {'form': form})
"""
def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Adicione logs para depuração
            print("Usuário salvo com sucesso!")
            return redirect('user_login')
        else:
            # Adicione logs para depuração
            print("Formulário inválido:", form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadastro.html', {'form': form})



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
