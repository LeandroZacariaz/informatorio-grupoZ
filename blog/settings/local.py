from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

'''
DATABASES = {
"default": {
"ENGINE": "django.db.backends.mysql",
"NAME": 'app_lectura',
"USER": 'root',
"PASSWORD": 'root',
"PORT": '3306'
}
} '''