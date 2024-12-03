import os
from pathlib import Path

# BASE_DIR define o diretório base do projeto, que é o diretório onde o arquivo settings.py está localizado.
BASE_DIR = Path(__file__).resolve().parent.parent

# A chave secreta do Django para garantir a criptografia e segurança do sistema. Em produção, é importante definir essa chave no ambiente e não deixá-la no código.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-ligc=s16#4g=6u5qbnx1rqc@pz*4oj1*in4aa3@o67g6(gg)o7')

# Em modo de produção, a variável DEBUG deve ser definida como False para não expor informações sensíveis.
DEBUG = False

# A lista de hosts permitidos para o seu projeto. Em produção, você deve especificar os domínios que são permitidos para acessar o site.
ALLOWED_HOSTS = ['senac-django-project.vercel.app', '.vercel.app', '127.0.0.1', 'localhost', '127.0.0.1:8000']

# URLs para login, redirecionamento após login e logout.
LOGIN_URL = '/accounts/login/'  # URL para a página de login
LOGIN_REDIRECT_URL = '/home/'  # Após o login, o usuário será redirecionado para esta página
LOGOUT_REDIRECT_URL = '/accounts/login/'  # Após o logout, o usuário será redirecionado para esta página

# INSTALLED_APPS lista todos os aplicativos Django e os personalizados que você está usando no seu projeto.
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # WhiteNoise serve arquivos estáticos
    'django.contrib.admin',  # Admin do Django
    'django.contrib.auth',  # Sistema de autenticação
    'django.contrib.contenttypes',  # Trabalha com tipos de conteúdo
    'django.contrib.sessions',  # Sessões de usuário
    'django.contrib.messages',  # Sistema de mensagens
    'django.contrib.staticfiles',  # Arquivos estáticos (CSS, JS)
    'contas',  # Seu app de contas de usuário
    'core',  # App principal do seu projeto
]

# MIDDLEWARE define os componentes de middleware usados no projeto. 
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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ROOT_URLCONF especifica o arquivo principal de URLs que mapeia as requisições HTTP para as views.
ROOT_URLCONF = 'senac_django_project.urls'

# TEMPLATES configura o mecanismo de templates. Aqui você define onde o Django procurará os templates HTML.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # O backend de templates do Django
        'DIRS': [BASE_DIR / 'templates'],  # Diretórios onde os templates serão procurados
        'APP_DIRS': True,  # Permite que o Django procure por templates dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Processador de contexto para debug
                'django.template.context_processors.request',  # Processador de contexto para requisições
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',  # Processador de contexto para autenticação
                'django.contrib.messages.context_processors.messages',  # Processador de contexto para mensagens
            ],
        },
    },
]

# WSGI_APPLICATION especifica o caminho para o arquivo WSGI, que é usado para implantar o Django.
WSGI_APPLICATION = 'senac_django_project.wsgi.application'

# DATABASES configura o banco de dados do Django. Aqui estamos usando o banco de dados SQLite para desenvolvimento.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # O backend de banco de dados SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # O arquivo do banco de dados no diretório do projeto
    }
}

# AUTHENTICATION_BACKENDS define os backends de autenticação. Aqui estamos usando o backend padrão de autenticação do Django.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Para autenticação normal de usuários
]

# AUTH_PASSWORD_VALIDATORS define as validações de senha a serem aplicadas.
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

# LANGUAGE_CODE define o idioma do projeto. A configuração 'pt-br' é para português do Brasil.
LANGUAGE_CODE = 'pt-br'

# TIME_ZONE define o fuso horário do projeto. Aqui, o fuso horário é definido para São Paulo.
TIME_ZONE = 'America/Recife'

# Configurações de internacionalização e fuso horário.
USE_I18N = True
USE_TZ = True

# STATIC_URL define a URL pública onde os arquivos estáticos podem ser acessados.
STATIC_URL = '/static/'

# STATICFILES_DIRS define onde o Django procurará arquivos estáticos adicionais durante o desenvolvimento.

# Configuração para servir os arquivos estáticos em produção
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configurações para arquivos de mídia (arquivos carregados pelos usuários).
MEDIA_URL = '/media/'  # URL para acessar os arquivos de mídia
MEDIA_ROOT = BASE_DIR / 'media'  # Diretório onde os arquivos de mídia serão armazenados

# Define o tipo de campo primário a ser usado para modelos. `BigAutoField` é recomendado para garantir IDs maiores.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
