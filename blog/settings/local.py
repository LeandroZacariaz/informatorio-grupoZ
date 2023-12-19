from .base import *


DEBUG = True

ALLOWED_HOSTS = ['LeandroMZ.pythonanywhere.com']



DATABASES = {
        "default": {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": 'LeandroMZ$infogZ',
        "USER": 'LeandroMZ',
        "PASSWORD": 'root12345',
        "HOST": 'LeandroMZ.mysql.pythonanywhere-services.com',
        "PORT": '3306',
                    }
            }
