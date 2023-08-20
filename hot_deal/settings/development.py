from .base import *

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
