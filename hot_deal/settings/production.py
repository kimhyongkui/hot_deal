from .base import *

DEBUG = False

ALLOWED_HOSTS = ['my domain']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hot_deal',
        'USER': 'root',
        'PASSWORD': '0000',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}