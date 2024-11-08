\senac_django_project
│
├── contas/                # App 'contas'
│   ├── migrations/        # Migrações do banco de dados
│   ├── __init__.py        # Inicializa o pacote
│   ├── admin.py           # Admin do Django para gerenciamento do app
│   ├── apps.py            # Configurações do app
│   ├── forms.py           # Formulários do app
│   ├── models.py          # Modelos de dados do app
│   ├── tests.py           # Testes do app
│   ├── urls.py            # URLs do app 'contas'
│   ├── views.py           # Views do app 'contas'
│   └── templates/         # Templates relacionados ao app
│       └── accounts/
│           ├── signup.html  # Template de cadastro
│           └── login.html   # Template de login
│
├── core/                  # App 'core' com funcionalidades principais
│   ├── migrations/        # Migrações do banco de dados
│   ├── __init__.py        # Inicializa o pacote
│   ├── admin.py           # Admin do Django para gerenciamento do app
│   ├── apps.py            # Configurações do app
│   ├── models.py          # Modelos de dados do app
│   ├── tests.py           # Testes do app
│   ├── urls.py            # URLs do app 'core'
│   └── views.py           # Views do app 'core'
│
├── senac_django_project/  # Pasta principal do projeto
│   ├── __init__.py        # Inicializa o pacote
│   ├── settings.py        # Configurações principais do Django
│   ├── urls.py            # URLs principais do projeto
│   └── wsgi.py            # WSGI application para deploy
│
├── .gitignore             # Arquivo para ignorar arquivos do Git
├── db.sqlite3             # Banco de dados SQLite
├── manage.py             # Script de gerenciamento do Django
├── pastas.md             # Documentação sobre as pastas do projeto
├── README.md             # Documento de descrição do projeto
├── requirements.txt      # Dependências do projeto
├── settings.md           # Documentação sobre as configurações do projeto
└── vercel.json           # Arquivo de configuração do Vercel para deploy
