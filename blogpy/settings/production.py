from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blogpykc.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2o013g2qaa9in',
        'USER': 'ccreruskvsyjuo',
        'PASSWORD': 'fc901d6baa2deedbc0dbc56fbe5663b2842a7188012fab7fc689c590329b542e',
        'HOST': 'ec2-23-21-109-177.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')