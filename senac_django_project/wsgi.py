import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'senac_django_project.settings')

try:
    # Configuração da aplicação WSGI padrão do Django
    application = get_wsgi_application()

    # Configurando o WhiteNoise para servir arquivos estáticos
    application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'staticfiles'))
except Exception as e:
    # Imprime o erro no console para depuração
    print(f"Erro ao carregar WSGI application: {e}", file=sys.stderr)
    raise
