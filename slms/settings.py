import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta, deve ser mantida em segurança (recomenda-se usar variáveis de ambiente para produção)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-8j+nu3y0_ab%bhda_(x3=8&!a+s^!czew#-b2m#1m(-g#$uaya')

DEBUG = True  # Para produção, altere para False e configure o DEBUG via variáveis de ambiente

ALLOWED_HOSTS = ['rh-sistema.fly.dev', '127.0.0.1', 'localhost', '*']

CSRF_TRUSTED_ORIGINS = [
    'https://sistemalicenca.fly.dev',
    'http://sistemalicenca.fly.dev',  # Se também for necessário permitir a versão HTTP
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slmsapp',  # Sua app personalizada
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'slms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'slms.wsgi.application'

# Configuração do banco de dados, com volume montado no Fly.io
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senha
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

# Localização, fuso horário e internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuração dos arquivos estáticos
STATIC_URL = '/static/'

# Usando o WhiteNoise para servir os arquivos estáticos em produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Caminho onde os arquivos estáticos serão armazenados (em produção no Fly.io, o caminho será /code/static)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Modelo de usuário personalizado
AUTH_USER_MODEL = 'slmsapp.CustomUser'

