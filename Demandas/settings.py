import dj_database_url
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x9oa2%q4zg^@hyo*hr@4roxp9d3)ync($!k#_axr)=!l39nall'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demanda',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
   
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Demandas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Demandas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



# Use a URL environment variable if available, otherwise use the specified values
DATABASE_URL = os.getenv("DATABASE_URL")
# Adicione o seguinte bloco condicional
if DATABASE_URL:
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)}
else:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}



"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'demanda.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,  # Defina o comprimento mínimo da senha desejado
        }
    },
    # Adicione outras validações conforme necessário
]

"""
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]
"""



# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-Br'

TIME_ZONE = 'America/Manaus'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

WHITENOISE_USE_FINDERS = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Substitua os valores conforme necessário
DEFAULT_FROM_EMAIL = 'bragasan34@gmail.com'
EMAIL_RECEPIENT = ['bragasan1@gmail.com']

# Lembre-se de configurar corretamente suas credenciais de e-mail no seu servidor SMTP
EMAIL_BACKEND = 'django.core.magil.backends.smtp.EmailBackend'
#EMAIL_HOST = 'mail.sesiam.org.br'  # provedor de e-mail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # porta do provedor de e-mail
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'bragasan34@gmail.com'  # Substitua pelo seu email
#EMAIL_HOST_PASSWORD = 'fieam@2023'
EMAIL_HOST_PASSWORD = 'eptk mfkd mfgk mfqg '

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'demanda.backends.CaseInsensitiveModelBackend',
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True









