from .base import *

ALLOWED_HOSTS = []

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
