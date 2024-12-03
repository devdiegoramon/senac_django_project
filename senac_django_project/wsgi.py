import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'senac_django_project.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    # Imprime o erro no console para depuração
    print(f"Erro ao carregar WSGI application: {e}", file=sys.stderr)
    raise