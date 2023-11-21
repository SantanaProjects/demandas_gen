from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Se o nome de usuário não estiver definido, retorne None
        if username is None:
            return None

        # Busque o usuário no banco de dados sem diferenciar maiúsculas e minúsculas
        user = UserModel.objects.filter(username__iexact=username).first()

        # Verifique a senha, se o usuário for encontrado
        if user is not None and user.check_password(password):
            return user