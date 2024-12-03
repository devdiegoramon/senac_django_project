from senac_django_project.wsgi import application
from whitenoise import WhiteNoise

# Adicione suporte ao WhiteNoise
application = WhiteNoise(application, root="static")

# Defina o handler esperado pela Vercel
app = application
