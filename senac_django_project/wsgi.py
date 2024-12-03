# wsgi.py

from senac_django_project.wsgi import application
from whitenoise import WhiteNoise

# Adicione o WhiteNoise para servir arquivos estáticos
application = WhiteNoise(application, root="static")

# Permite o uso de arquivos comprimidos para melhorar a performance
application.add_files("static", prefix="static/")
