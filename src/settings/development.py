import os

from src.settings.local import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Nomad',
        'USER': 'postgres',
        'PASSWORD': 'letmein20116199623',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
