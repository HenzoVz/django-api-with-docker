# django-api-with-docker

API em Django utilizando container docker para executar uma instância do PostgreSQL

#### Criando container docker do PostgreSQL 

* docker run --name database -e POSTGRES_PASSWORD= password -p 5432:5432 -d postgres

#### Configuração do banco de dados dentro *settings.py* 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'database_name'),
        'USER': os.environ.get('DB_USER', 'database_user'),
        'PASSWORD': os.environ.get('DB_PASS', 'database_password'),
        'HOST': 'localhost',
        'PORT': '5432',
     }
 }
