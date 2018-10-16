from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'checkmate',
        'USER': 'root', 
        'PASS': 'CpS$@)Team2',
        'HOST': '18.222.239.255'
    }
}